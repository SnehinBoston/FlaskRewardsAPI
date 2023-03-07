import app
import json
import unittest
class RewardsTest(unittest.TestCase):
    def setUp(self):
        self.db_uri = 'sqlite:///test.db'
        self.app = app.app
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.db = app.db
        self.db.create_all()
        self.client = self.app.test_client()
        
    def test_addSales(self):
        # payload = json.loads(json.dumps({
        #     "customerId" : 9,
        #     "amount": 200,
        #     "weekNo": 9, 
        #     "points": 0
        # }))
        response = self.client.post('/addSales')
        # data = dict(customerId = 9, amount = 200, weekNo = 9, points = 0), follow_redirects=True
        self.assertEqual(201, response.status_code)
        # self.assertEqual(9, json.loads(json.dumps(response))['customerId'])
        # self.assertEqual(200, response.json['amount'])
        # self.assertEqual(9, response.json['weekNo'])
        # self.assertEqual(0, response.json['points'])
        # self.assertEqual(200, response.status_code)
    
    def test_allCustomerRewards(self):
        response = self.app.get('/allCustomerRewards', headers = {"Conent-Type": 'application/json'})
        # self.assertEqual(9, response.json['customerId'])

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()
if __name__ == '__main__':
    unittest.main()


# # import os
# # import tempfile

# # import pytest

# # import app

# # @pytest.fixture
# # def client():
# #     db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
    
# #     app.app.config['TESTING'] = True

# #     with app.app.test_client() as client:
# #         # with app.app.app_context():
# #         #     app.db.init_app(app.app)
# #         yield client
# #     os.close(db_fd)
# #     os.unlink(app.app.config['DATABASE'])

# # def test_empty_db(client):
# #     rv = client.get('/')
    
# #     assert b"<p>Flask Rewards API</p>" in rv.data


# # from contextlib import contextmanager
# # from flask import appcontext_pushed, g

# # def get_sales():
# #     sale = getattr(g, 'sale', None)
# #     if sale is None:
# #         sale = fetch_current_
# # def get_user():
# #     user = getattr(g, 'user', None)
# #     if user is None:
# #         user = fetch_current_user_from_database()
# #         g.user = user
# #     return user

# # @contextmanager
# # def sales_set(app, sales):
# #     def handler(sender, **kwargs):
# #         g.Sales = sales
# #     with appcontext_pushed.connected_to(handler, app):
# #         yield

# # from flask import json, jsonify
# # import rewards
# # # @app.post('/addSales')
# # # def addSales():
# # #     return 
# # # @app.route('/users/me')
# # # def users_me():
# # #     return jsonify(username=g.user.username)
# # with sales_set(app, my_sales):



# # with user_set(app, my_user):
# #     with app.test_client() as c:
# #         resp = c.get('/users/me')
# #         data = json.loads(resp.data)
# #         self.assert_equal(data['username'], my_user.username)




# # import os

# # def test_spy_function(mocker):
# #     # mymodule declares `myfunction` which just returns 42
# #     import rewards

# #     spy = mocker.spy(rewards, "")
# #     assert rewards.myfunction() == 42
# #     assert spy.call_count == 1
# #     assert spy.spy_return == 42

# # class UnixFS:

# #     @staticmethod
# #     def rm(filename):
# #         os.remove(filename)

# # def test_unix_fs(mocker):
# #     mocker.patch('os.remove')
# #     UnixFS.rm('file')
# #     os.remove.assert_called_once_with('file')


# # def test_db(client):
# #     rv = client.get('/addSales')
    
# #     assert b"" in rv.data

# # def test_unix_fs(mocker):
# #     mocker.patch('os.remove')
# #     UnixFS.rm('file')
# #     os.remove.assert_called_once_with('file')

# import pytest
# import json
# import os
# import tempfile

# import app

# @pytest.fixture
# def client():
#     db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
#     app.app.config['TESTING'] = True

#     with app.app.test_client() as client:
#         with app.app.app_context():
#             app.db.init_app(app.app)
#         yield client

#     os.unlink(app.app.config['DATABASE'])
#     os.close(db_fd)

# def test_empty_db(client):
#     rv = client.get('/')
#     assert b'<p>Flask Rewards API</p>' in rv.data

# def test_new_sale():
#     user = User('patkennedy79@gmail.com', 'FlaskIsAwesome')
#     assert user.email == 'patkennedy79@gmail.com'
#     assert user.hashed_password != 'FlaskIsAwesome'
#     assert user.role == 'user'