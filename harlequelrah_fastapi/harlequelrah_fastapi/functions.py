# retourne les attributs d"un model
def attribut(MyModel):
    model_attributes = [
        attr
        for attr in dir(MyModel)
        if not callable(getattr(MyModel, attr)) and not attr.startswith("__")
    ]
    return model_attributes
