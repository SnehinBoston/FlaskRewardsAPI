from flask import Flask, Blueprint, render_template, request, redirect
import json
from flask import jsonify
from flask_smorest import abort
import json
rw = Blueprint('rewards', __name__)
import schemas
import app
import models
Sales_serializer = schemas.SalesSchema(many=True)

def dumper_for_response(obj):
    return Sales_serializer.dumps(obj, many=True)

def dumper_for_calc(obj):
    return Sales_serializer.dump(obj, many = True)

def customerTransactionsByMonth(customerId, initWeek, endWeek):
    monthlyCustomerTransactions = dumper_for_calc(models.Sales.query.filter((models.Sales.weekNo >=initWeek) & (models.Sales.weekNo <=endWeek) & (models.Sales.customerId == customerId)).all())
    total_points = 0
    for transaction in monthlyCustomerTransactions:
        if transaction['amount'] > 100:
            transaction['points'] = (transaction['amount'] - 100) * 2
            transaction['points'] += 1
        if transaction['amount'] > 50:
            transaction['points'] += 1
        total_points += transaction['points']
    return total_points

def customerRewardsCalculator(customerId):
    customerRewards = {}
    customerRewards[customerId] = [customerTransactionsByMonth(customerId, 1, 4), customerTransactionsByMonth(customerId, 5, 8), customerTransactionsByMonth(customerId, 8, 12)]
    customerRewards[customerId].append(customerRewards[customerId][0] + customerRewards[customerId][1] + customerRewards[customerId][2])
    return customerRewards

@rw.post('/addSales')
def addSales():
    sales = json.loads(json.dumps(request.get_json()))
    for sale in sales:
        sale_obj = models.Sales(customerId=sale['customerId'], amount=sale['amount'],
                       weekNo=sale['weekNo'], points=sale['points'])
        app.db.session.add(sale_obj)
        app.db.session.commit()
    sales_db_data = models.Sales.query.all()
    sales_dump_data = dumper_for_response(sales_db_data)
    return sales_dump_data, 201   

@rw.get('/allCustomerRewards')
def allCustomerRewards():
    allCustomerRewards = {}
    for customerId in models.Sales.query.with_entities(models.Sales.customerId).distinct():
        customerData = customerRewardsCalculator(customerId[0])
        allCustomerRewards[customerId[0]] = customerData[customerId[0]][-1]
    return allCustomerRewards

@rw.get('/rewards/<int:customerId>')
def customerRewards(customerId):
    customerRewards = {}
    customerRewards = customerRewardsCalculator(customerId)
    return jsonify({"Customer: ": customerId, "Month 1": customerRewards[customerId][0], "Month 2 : ": customerRewards[customerId][1], "Month 3 : ": customerRewards[customerId][2], "Total rewards : ": customerRewards[customerId][3]})

@rw.get('/getTransactions/<int:customerId>')
def getTransactionsPerCustomer(customerId):
    customer_transactions = models.Sales.query.filter_by(customerId = customerId).all()
    return dumper_for_response(customer_transactions)

# Future flavor - add category
# @rw.get("/")


