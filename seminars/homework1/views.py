import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def home(request):
    home_html_text = """
        <a href="/homework1">Главная</a> <a href="/homework1/about">Обо мне</a>
        <h1>Мой сайт</h1>
        <p>Egestas purus viverra accumsan in nisl nisi scelerisque. Faucibus pulvinar elementum integer
         enim neque volutpat ac. Nisl condimentum id venenatis a condimentum vitae sapien pellentesque.
         Arcu odio ut sem nulla pharetra diam sit amet nisl. Sapien nec sagittis aliquam malesuada
         bibendum arcu. Hac habitasse platea dictumst vestibulum rhoncus est pellentesque. Dignissim
         cras tincidunt lobortis feugiat vivamus. Vel elit scelerisque mauris pellentesque pulvinar 
         pellentesque habitant. Placerat in egestas erat imperdiet. Convallis a cras semper auctor
         neque vitae tempus. Quisque id diam vel quam elementum pulvinar. Pharetra convallis posuere
         morbi leo. Venenatis cras sed felis eget velit aliquet. Metus vulputate eu scelerisque felis
         imperdiet proin fermentum.</p>
     """
    logger.info("Visited page home")
    return HttpResponse(home_html_text)


def about(request):
    about_html_text = """
        <a href="/homework1">Главная</a> <a href="/homework1/about">Обо мне</a>
        <h1>Обо мне</h1>
        <p>Dolor magna eget est lorem ipsum dolor sit. Ultrices neque ornare aenean euismod elementum.
         Lectus arcu bibendum at varius. Purus viverra accumsan in nisl nisi. Dui id ornare arcu odio
         ut sem nulla. Tortor at risus viverra adipiscing. Adipiscing elit pellentesque habitant morbi
         tristique senectus et. Aliquam id diam maecenas ultricies mi eget mauris. Ut sem viverra aliquet
         eget sit amet tellus cras. Lectus vestibulum mattis ullamcorper velit sed. Dapibus ultrices in
         iaculis nunc sed augue.</p>
    """
    logger.info("Visited page about")
    return HttpResponse(about_html_text)
