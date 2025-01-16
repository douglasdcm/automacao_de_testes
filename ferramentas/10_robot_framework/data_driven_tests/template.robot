*** Settings ***
Documentation     Resusable Test Case (Data-Driven).
Library           SeleniumLibrary
Test Teardown     Close Browser

*** Variables ***
${LOGIN URL}        http://www.google.com
${BROWSER}          Chrome
${VALID PASSWORD}   foo
${VALID USER}       foo

*** Test Cases ***
Search terms related to automation testing
    [Template]    Search terms on Google
    cheese
    selenium
    robot framework

*** Keywords ***
Search terms on Google
    [Arguments]    ${TERM}
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Google
    Input Text     q    ${TERM}
    Wait Until Element Is Enabled   btnK
    Press Key   xpath://body    ESC
    Click Button   btnK
    Wait Until Element Is Visible   css:#logo
    Element Attribute Value Should Be   css:#logo   title    Ir para a página inicial do Google
    Close Browser