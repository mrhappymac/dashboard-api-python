# API key error
class APIKeyError(Exception):
    def __init__(self):
        self.message = 'Meraki API key needs to be defined'
        super(APIKeyError, self).__init__(self.message)

    def __repr__(self):
        return self.message


# To catch exceptions while making API calls
class APIError(Exception):
    def __init__(self, metadata, response):
        self.response = response
        self.tag = metadata['tags'][0]
        self.operation = metadata['operation']
        self.status = self.response.status_code if self.response else None
        self.reason = self.response.reason if self.response else None
        try:
            self.message = self.response.json() if self.response else None
        except ValueError:
            self.message = self.response.text[:100]
        super(APIError, self).__init__(f'{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}')

    def __repr__(self):
        return f'{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}'

# To catch exceptions while making AIO API calls
class AsyncAPIError(Exception):
    def __init__(self, metadata, response, message):
        self.response = response
        self.tag = metadata['tags'][0]
        self.operation = metadata['operation']
        self.status = self.response.status if self.response else None
        self.reason = self.response.reason if self.response else None
        self.message = message[:100]
        super().__init__(
            f'{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}'
        )

    def __repr__(self):
        return f'{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}'
