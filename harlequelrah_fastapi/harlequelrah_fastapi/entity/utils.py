def update_entity(existing_entity, update_entity):
    for key, value in update_entity.dict().items():
        setattr(existing_entity, key, value)
