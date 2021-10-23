from peewee import *

db = DatabaseProxy()


class Status(Model):
    id = AutoField(primary_key=True)
    name = TextField()
    color = TextField()

    class Meta:
        database = db
        db_table = 'statuses'


class Tax(Model):
    id = AutoField(primary_key=True)
    name = TextField()
    tax_rate = IntegerField()

    class Meta:
        database = db
        db_table = 'taxes'


class Price(Model):
    id = AutoField(primary_key=True)
    gross_price = IntegerField()
    net_price = IntegerField()
    tax_amount = IntegerField()
    tax = ForeignKeyField(Tax)

    class Meta:
        database = db
        db_table = "prices"


class Invoice(Model):
    id = AutoField(primary_key=True)
    number = TextField()
    create_date = DateField()
    due_date = DateField()
    price = ForeignKeyField(Price)

    class Meta:
        database = db


class IDebit(Invoice):
    pass


class IKredit(Invoice):
    pass

class IReceipt(Invoice):
    pass
