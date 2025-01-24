from services import plovdiv24, mailbg, techoffnews, econt, abv_scraper, sportal
from services import arenabg, pomagalo, teenproblem, dnevnik, burgas24
from services import varna24, mediapool, chitanka, forlife, vitamag
from services import bgeprosveta

SCRAPERS = {
    "ABV.bg": abv_scraper.check_username_registration,
    "e-prosveta": bgeprosveta.check_username_registration,
    "Plovdiv24.bg": plovdiv24.check_username_registration,
    "Mail.bg": mailbg.check_username_registration,
    "Offmedia.bg": techoffnews.check_username_registration,
    "Econt.com": econt.check_username_registration,
    "Sportal.bg": sportal.check_username_registration,
    "Arenabg.com": arenabg.check_username_registration,
    "Pomagalo.com": pomagalo.check_username_registration,
    "Teenproblem.net": teenproblem.check_username_registration,
    "Dnevnik.bg": dnevnik.check_username_registration,
    "Burgas24.bg": burgas24.check_username_registration,
    "Varna24.bg": varna24.check_username_registration,
    "Mediapool.bg": mediapool.check_username_registration,
    "Chitanka.info": chitanka.check_username_registration,
    "Vitamag.bg": vitamag.check_username_registration,
    "Forlife.bg": forlife.check_username_registration,
}