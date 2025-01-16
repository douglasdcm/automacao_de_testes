*** Settings ***
Documentation     Resusable Keywords.
Library           SeleniumLibrary
Library           DataDriver

*** Variables ***
${LOGIN URL}      http://www.google.com
${BROWSER}        Chrome

*** Keywords ***
Open Browser To Search Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Google

Search Term
    [Arguments]    ${term}
    Input Text     q    ${term}
    Wait Until Element Is Enabled   btnK
    Press Key   xpath://body    ESC
    Click Button   btnK

All Tab Should Be Open
    Wait Until Element Is Visible   css:#logo
    Element Attribute Value Should Be   css:#logo   title    Ir para a página inicial do Google