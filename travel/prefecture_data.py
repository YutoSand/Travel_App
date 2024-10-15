class Prefecture:
    def __init__(self, name, categories, urban_rural, climate, is_cheap, is_active):
        self.name = name
        self.categories = categories
        self.urban_rural = urban_rural
        self.climate = climate
        self.is_cheap = is_cheap
        self.is_active = is_active

    def has_interest(self, interest):
        return interest.lower() in self.categories