class AsyncOpenAPISpec:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getOrganizationOpenapiSpec(self, organizationId: str):
        """
        **Return the OpenAPI 2.0 Specification of the organization's API documentation in JSON**
        https://api.meraki.com/api_docs#return-the-openapi-2
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['OpenAPI Spec'],
            'operation': 'getOrganizationOpenapiSpec',
        }
        resource = f'/organizations/{organizationId}/openapiSpec'

        return await self._session.get(metadata, resource)

