import app
import models
class SalesSchema(app.ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Sales
        ordered = True