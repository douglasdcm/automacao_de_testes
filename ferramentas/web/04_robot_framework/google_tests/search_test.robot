*** Settings ***
Documentation     Search the terms on Google.
Resource          ./resources.robot

*** Test Cases ***
Search cheese
    Open Browser To Search Page
    Search Term    cheese
    All Tab Should Be Open
    [Teardown]    Close Browser
