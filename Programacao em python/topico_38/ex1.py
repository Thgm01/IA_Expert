import re
def find_cel_numbers(phrase):
    phrase = str(phrase)
    results = re.findall('\(\d{2,3}\)\d{4,5}-\d{4}', phrase)
    return results

def find_cep(phrase):
    phrase = str(phrase)
    results = re.findall('\d{5}-\d{3}', phrase)
    return results

def find_url(phrase):
    phrase = str(phrase)
    results = re.findall('https?://[A-Za-z0-9./]+', phrase)
    return results

phrase = 'Bella Mia Ateliê shared a photo on Instagram: “Novo número para contato! (19)99560-9569 ☆ Adicione na sua lista! Ligue ou nos mande uma…” • See 1,274 photos and videos on their profile. '
phrase2 = 'Rua Guiratinga	Cidade Alta	Cuiabá/MT	78030-443'
url='https://www.techtudo.com.br/noticias/2014/10/lista-tem-10-urls-do-google-que-voce-deveria-dar-mais-atencao-veja.ghtml'

print(find_cel_numbers(phrase))
print(find_cep(phrase2))
print(find_url(url))