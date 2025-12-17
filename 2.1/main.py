from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    orders = relationship('Order', back_populates='client')

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    product = Column(String(100), nullable=False)
    quantity = Column(Integer)
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship('Client', back_populates='orders')

engine = create_engine('sqlite:///simple_shop.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

clients_data = [
    {'name': 'qwerty'},
    {'name': 'asdfgh'},
    {'name': 'zxcvbn'},
    {'name': 'poiuyt'},
    {'name': 'lkjhgf'}
]

clients = []
for client_info in clients_data:
    client = Client(name=client_info['name'])
    session.add(client)
    clients.append(client)

session.flush()

orders_data = [
    {'product': 'item_abc', 'quantity': 3, 'client_id': clients[0].id},
    {'product': 'item_xyz', 'quantity': 5, 'client_id': clients[0].id},
    {'product': 'item_test', 'quantity': 2, 'client_id': clients[1].id},
    {'product': 'item_sample', 'quantity': 7, 'client_id': clients[2].id},
    {'product': 'item_demo', 'quantity': 1, 'client_id': clients[2].id},
    {'product': 'item_temp', 'quantity': 4, 'client_id': clients[3].id},
    {'product': 'item_data', 'quantity': 6, 'client_id': clients[4].id}
]

for order_info in orders_data:
    order = Order(
        product=order_info['product'],
        quantity=order_info['quantity'],
        client_id=order_info['client_id']
    )
    session.add(order)

session.commit()

all_clients = session.query(Client).all()

for client in all_clients:
    print(f"\nКлиент: {client.name}")
    if client.orders:
        for order in client.orders:
            print(f"Заказ: {order.product} (количество: {order.quantity})")
    else:
        print("  Нет заказов")
session.close()