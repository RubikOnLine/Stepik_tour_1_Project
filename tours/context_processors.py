
def departure_for_menu(request):

    return {'menu_list': {
                          "msk": "Из Москвы",
                          "spb": "Из Петербурга",
                          "nsk": "Из Новосибирска",
                          "ekb": "Из Екатеринбурга",
                          "kazan": "Из Казани"
                          }
           }



def descript_list(request):

    return {'title_from_c_p': "Stepik Travel",
            'subtitle_from_c_p': "Для тех, кого отвлекают дома",
            'description_from_c_p': "Лучшие направления, где никто не будет вам мешать сидеть на берегу и изучать программирование, дизайн, разработку игр и управление продуктами",
            'display_from_c_p': "Всякие туры"
             }
