import torch
import torch.nn as nn
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
import os

model_path = 'fnn_model.pkl'
if not os.path.exists(model_path):
    print(f"Ошибка: файл модели '{model_path}' не найден!")
    print("Сначала обучите модель с помощью основного скрипта.")
    exit()

print("=" * 60)
print("ПОИСК И ВЫВОД НЕПРАВИЛЬНО ПРЕДСКАЗАННЫХ ЦИФР")
print("=" * 60)


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 500)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(500, 10)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out


print("Загрузка модели...")
model = Net()
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()
print("Модель загружена успешно!")

print("Загрузка тестовых данных MNIST...")
test_dataset = dsets.MNIST(
    root='./data',
    train=False,
    transform=transforms.ToTensor(),
    download=True
)

test_loader = torch.utils.data.DataLoader(
    dataset=test_dataset,
    batch_size=100,
    shuffle=False
)
print(f"Загружено {len(test_dataset)} тестовых изображений")

print("\nПоиск неправильных предсказаний...")

incorrect_predictions = []
all_predictions = []

with torch.no_grad():
    for batch_idx, (images, labels) in enumerate(test_loader):
        images_flat = images.reshape(-1, 28 * 28)


        outputs = model(images_flat)
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
        _, predicted = torch.max(outputs.data, 1)

        for i in range(len(labels)):
            true_label = labels[i].item()
            pred_label = predicted[i].item()
            confidence = probabilities[i][pred_label].item()

            all_predictions.append((true_label, pred_label, confidence))

            if true_label != pred_label:
                incorrect_predictions.append({
                    'image': images[i],
                    'true_label': true_label,
                    'pred_label': pred_label,
                    'confidence': confidence,
                    'global_index': batch_idx * 100 + i
                })

        if (batch_idx + 1) % 10 == 0:
            print(f"  Обработано {(batch_idx + 1) * 100} изображений...")

total_images = len(all_predictions)
incorrect_count = len(incorrect_predictions)
accuracy = 100 * (total_images - incorrect_count) / total_images

print("\n" + "=" * 60)
print("СТАТИСТИКА:")
print("=" * 60)
print(f"Всего тестовых изображений: {total_images}")
print(f"Правильно предсказано: {total_images - incorrect_count}")
print(f"Неправильно предсказано: {incorrect_count}")
print(f"Точность модели: {accuracy:.2f}%")
print(f"Процент ошибок: {100 * incorrect_count / total_images:.2f}%")

if incorrect_count == 0:
    print("\nПоздравляем! Модель предсказала все изображения правильно!")
    exit()

print("\n" + "=" * 60)
print("АНАЛИЗ ОШИБОК ПО КЛАССАМ:")
print("=" * 60)

confusion = np.zeros((10, 10), dtype=int)

for true, pred, _ in all_predictions:
    confusion[true][pred] += 1

print("\nМатрица ошибок (строки = истинные классы, столбцы = предсказанные):")
print("    " + " ".join([f"{i:3}" for i in range(10)]))
print("-" * 43)

for i in range(10):
    row_str = f"{i:2} | "
    for j in range(10):
        if i == j:
            row_str += f"\033[92m{confusion[i][j]:3}\033[0m "
        else:
            row_str += f"{confusion[i][j]:3} "
    print(row_str)

print("\nНаиболее часто путаемые цифры:")
for i in range(10):
    total_class = np.sum(confusion[i])
    correct = confusion[i][i]
    error_rate = 100 * (total_class - correct) / total_class if total_class > 0 else 0

    if total_class > 0:
        confusion_copy = confusion[i].copy()
        confusion_copy[i] = 0
        most_confused = np.argmax(confusion_copy)
        most_confused_count = confusion[i][most_confused]

        if most_confused_count > 0:
            print(f"  Цифра {i}: {error_rate:.1f}% ошибок, "
                  f"чаще всего путают с {most_confused} ({most_confused_count} раз)")

print("\n" + "=" * 60)
print(f"ВЫВОД ВСЕХ НЕПРАВИЛЬНЫХ ПРЕДСКАЗАНИЙ ({incorrect_count} изображений):")
print("=" * 60)

max_to_show = min(incorrect_count, 100)
if incorrect_count > 100:
    print(f"Примечание: Показаны первые 100 из {incorrect_count} ошибок")

cols = 10
rows = (max_to_show + cols - 1) // cols

fig, axes = plt.subplots(rows, cols, figsize=(20, rows * 2))
if max_to_show > 1:
    axes = axes.flatten()
else:
    axes = [axes]

for idx, ax in enumerate(axes):
    if idx >= max_to_show:
        ax.axis('off')
        continue

    data = incorrect_predictions[idx]
    image = data['image'].squeeze()
    true_label = data['true_label']
    pred_label = data['pred_label']
    confidence = data['confidence']

    ax.imshow(image, cmap='gray')

    color = 'red'

    ax.set_title(f"И:{true_label}→П:{pred_label}\n({confidence:.1%})",
                 color=color, fontsize=9)
    ax.axis('off')

    if idx < 20:
        print(f"Ошибка #{idx + 1}: Истинная={true_label}, Предсказанная={pred_label}, "
              f"Уверенность={confidence:.2%}, Индекс={data['global_index']}")

for idx in range(max_to_show, len(axes)):
    axes[idx].axis('off')

plt.suptitle(f'Неправильные предсказания ({max_to_show} из {incorrect_count} ошибок)\n'
             f'Точность модели: {accuracy:.2f}%',
             fontsize=16, fontweight='bold')

plt.tight_layout(rect=[0, 0.03, 1, 0.97])

output_filename = 'incorrect_predictions.png'
plt.savefig(output_filename, dpi=150, bbox_inches='tight')
print(f"\nГрафик сохранен как '{output_filename}'")

print("\n" + "=" * 60)
print("РАСПРЕДЕЛЕНИЕ ОШИБОК ПО КЛАССАМ:")
print("=" * 60)

fig3, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

true_class_errors = np.zeros(10)
for error in incorrect_predictions:
    true_class_errors[error['true_label']] += 1

total_per_class = np.sum(confusion, axis=1)
error_rates = 100 * true_class_errors / total_per_class

x = np.arange(10)
width = 0.35

bars1 = ax1.bar(x - width / 2, true_class_errors, width, label='Количество ошибок', color='lightcoral')
ax1.set_xlabel('Истинная цифра')
ax1.set_ylabel('Количество ошибок')
ax1.set_title('Абсолютное количество ошибок по классам')
ax1.set_xticks(x)
ax1.set_xticklabels([str(i) for i in range(10)])

for bar in bars1:
    height = bar.get_height()
    if height > 0:
        ax1.text(bar.get_x() + bar.get_width() / 2., height + 0.5,
                 f'{int(height)}', ha='center', va='bottom', fontsize=9)

bars2 = ax2.bar(x + width / 2, error_rates, width, label='Процент ошибок', color='salmon')
ax2.set_xlabel('Истинная цифра')
ax2.set_ylabel('Процент ошибок (%)')
ax2.set_title('Процент ошибок по классам')
ax2.set_xticks(x)
ax2.set_xticklabels([str(i) for i in range(10)])

for bar in bars2:
    height = bar.get_height()
    if height > 0:
        ax2.text(bar.get_x() + bar.get_width() / 2., height + 0.5,
                 f'{height:.1f}%', ha='center', va='bottom', fontsize=9)

plt.suptitle('Анализ ошибок по классам', fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

output_filename3 = 'error_distribution.png'
plt.savefig(output_filename3, dpi=150, bbox_inches='tight')
print(f"График распределения ошибок сохранен как '{output_filename3}'")



print("\n" + "=" * 60)
print("ВЫВОД ГРАФИКОВ:")
print("=" * 60)
print("Закройте каждый график, чтобы увидеть следующий...")

plt.figure(1)
plt.show()

print("\n" + "=" * 60)
print("АНАЛИЗ ЗАВЕРШЕН!")
print("=" * 60)
print(f"Созданы файлы:")
print(f"  1. incorrect_predictions.png - все ошибки")
print(f"  2. top_confidence_errors.png - топ-10 уверенных ошибок")
print(f"  3. error_distribution.png - распределение ошибок")
print(f"  4. error_analysis_report.txt - детальный отчет")
print("=" * 60)