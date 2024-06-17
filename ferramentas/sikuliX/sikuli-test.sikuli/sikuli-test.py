text = "Hello world"

click(Region(358,77,182,28))
type("www.google.com")

# Garantir que a imagem não é confundida com outra.
# Esta imagem é o botão de pesquisar do campo de URL do browser,
# "1718592017012.png"
# mas está sendo confundida com o botão de voltar do browser.
# Mudei para usar o ENTER
# click()"1718591876605.png"
type(Key.ENTER)
wait(2)
click("1718591019203.png")
type(text)
click("1718590580080.png")
if not exists("1718591451379.png"):
    raise Exception("Not found.")

click("1718589344254.png")

