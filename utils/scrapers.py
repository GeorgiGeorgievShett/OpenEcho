from services import arenabg, abv, eprosveta, bittel, burgas24
from services import chitanka, cyberclubbg, dnevnik, econt
from services import essentiallybg, forlife, mailbg, mediapool
from services import plovdiv24, pomagalo, pragmaticbg, sportal
from services import teenproblem, trakiauniversity, vitamag
from services import varna24, techoffnews, fermoteka, zadoma
from services import elmak

SCRAPERS = {
    "ABV.bg": abv.check_username_registration,
    "Bg.e-prosveta.bg": eprosveta.check_username_registration,
    "Bittel.bg": bittel.check_username_registration,
    "Cyberclub.bg": cyberclubbg.check_username_registration,
    "Plovdiv24.bg": plovdiv24.check_username_registration,
    "Offmedia.bg": techoffnews.check_username_registration,
    "Econt.com": econt.check_username_registration,
    "Sportal.bg": sportal.check_username_registration,
    "Pragmatic.bg": pragmaticbg.check_username_registration,
    "Arenabg.com": arenabg.check_username_registration,
    "Pomagalo.com": pomagalo.check_username_registration,
    "Teenproblem.net": teenproblem.check_username_registration,
    "Dnevnik.bg": dnevnik.check_username_registration,
    "Burgas24.bg": burgas24.check_username_registration,
    "Varna24.bg": varna24.check_username_registration,
    "Mediapool.bg": mediapool.check_username_registration,
    "Vitamag.bg": vitamag.check_username_registration,
    "uni-sz.bg": trakiauniversity.check_ftt_username_registration,
    "Essentially.bg": essentiallybg.check_username_registration,
    "Fermoteka.bg": fermoteka.check_username_registration,
    "Za-doma.bg": zadoma.check_username_registration,
    "elmak.bg": elmak.check_username_registration,
    "Forlife.bg": forlife.check_username_registration,
    "Mail.bg": mailbg.check_username_registration,
    "Chitanka.info": chitanka.check_username_registration,
}