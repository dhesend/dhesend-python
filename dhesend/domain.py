from typing import TYPE_CHECKING, List
from re import match

from path import CREATE_DOMAIN_PATH, DELETE_DOMAIN_PATH, LIST_DOMAIN_PATH
from type import (
    DeleteDomainResponse, 
    FetchResponse, 
    CreateDomainResponse, 
    ListDomainDetail
)

if TYPE_CHECKING:
    from main import Dhesend
    
class Domain:
    def __init__(self, dhesend: "Dhesend"):
        self.dhesend = dhesend
    
    def create(self, domain_name: str) -> FetchResponse[CreateDomainResponse]:
        if not self.is_valid_domain(domain_name):
            return { 
                "data": None,
                "error": "Provide a valid domain, e.g., `xyz.com`."
            }
        
        return self.dhesend.post(path=CREATE_DOMAIN_PATH, body={ "domain": domain_name })
    
    def list(self) -> FetchResponse[List[ListDomainDetail]]:
        return self.dhesend.get(path=LIST_DOMAIN_PATH)
    
    def delete(self, domain_name: str) -> FetchResponse[DeleteDomainResponse]:
        return self.dhesend.post(path=DELETE_DOMAIN_PATH, body={ "domain": domain_name })
    
    def is_valid_domain(self, domain_name):
        regex = r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,6}$'
        return match(regex, domain_name) is not None