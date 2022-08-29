# Flask Web App Setup & Installtion Make sure you have the latest version of Python installed.

git clone <-URL->

- pip install
- Running The App python

```
-r pip_install.txt
python .\main.py
```

Viewing The App Go to http://127.0.0.1:5000
-----------------------------------------------------------
## Table of contents
* [About Project](#about-project)
* [Measured Values](#measured-values)
* [Technologies](#technologies)
* [Scheme](#scheme)
* [Docker](#docker)
* [For code reviewer](#for-code-reviewer)


-----------------------------------------------------------
# About Project

The MyHome_Telemetry project is about how much my house use: 
* water (dm3) per 24h/7d/e.t.c
* energu (kWh) to heat water use heat pump
* and also how much solar panels have produced energy.


The idea about this project come from my Father. His passion is teleinformatics, so i have something left from it ;)
So we bouht  nesessary meters connect to RasberyPi and start thinking how to make this whole staff work together.
The endpoint of this project i see like this. Using Flask/Django i will create website shows charts and other information and once a day bot will send push notification on phone (How much on that day house use water etc)

-----------------------------------------------------------
## Measured Values
* [Water](#water)
* [Heat Pump](#heat-pump)
* [Solaredge](#solaredge)

### Water
-----------------------------------------------------------

For wather measuring i use this water meter. Signal from register go to Anybus M-Bus/Modbus-TCP-Gateway by M-Bus where is convert to Modbus-TCP. From Anybus signal goes by to RasberyPi by TCP/IP protocol in LAN where bot (code in 'bots' file) written by me convert binary value to decimal value and send it to remote database every 5 min. 

-----------------------------------------------------------
![299819866_476893500568790_1032156745109520596_n](https://user-images.githubusercontent.com/44020188/185767357-36bae3b8-2d75-4846-8627-dfc2f47971b2.jpg)
![299748267_441129544697349_3292354809080360242_n](https://user-images.githubusercontent.com/44020188/185767350-104266fb-3bf5-45e2-9f71-47b57928bfff.jpg)
![300295083_596211648753536_1953649162381851983_n](https://user-images.githubusercontent.com/44020188/185767363-328519c8-a0f9-45a0-90e4-92e2b18389b7.jpg)


### Heat Pump 
-----------------------------------------------------------
In Heat Pump situation looks like this. The meter LE-03m is connecter to heat pump and measure how much HP consume energy. Then send singla use MODBUS by RS486  to converter which is connectet to RasberyPi where bot (code in 'bots' file) written by me conver input using this formula ( value = (r0 *(256*256) + r1 * 256 + r2)/10 ) to decimal number and send ist to remote database every 5 min .

Heat Pump also have more features. From HP signal by RS485 goes to 'black-box' and then goes to hub. Using RasberyPi we can read from HP values like: Temperature in boiler, temperature outside, temperature in/out and many many more (but right now i dont have idea/plan how to use this features :/)

LE-03M manual - https://www.fif.com.pl/pl/liczniki-zuzycia-energii-elektrycznej/339-licznik-zuzycia-energii-le-03m.html?fbclid=IwAR1bsHkWOV45t7rHKxRCWijoEu41s5mZq2mSojO2wou5koqmfIexHmO2TS0



-----------------------------------------------------------
![300527622_1450506268708443_1793216454363325692_n](https://user-images.githubusercontent.com/44020188/185767364-fde33aef-6c20-453e-b6d4-c1153b6e438e.jpg)
![299983697_3288583861412217_546950818204531387_n](https://user-images.githubusercontent.com/44020188/185767367-f9452846-3e50-463e-92bd-2198fca3bb31.jpg)
![299748267_441129544697349_3292354809080360242_n](https://user-images.githubusercontent.com/44020188/185767370-450c477b-0ed8-4d59-8b84-563cef1dd288.jpg)

### SolarEdge
-----------------------------------------------------------
To see how much solar panels produce energy i use API. At first we have to login to SolarEdge user panel, find API connection and just fallow the manual. I fount solution on the Internet. 
-----------------------------------------------------------
![299895812_1079271946315860_8938747832844990228_n](https://user-images.githubusercontent.com/44020188/185767341-c1df7c9c-cbab-4c3b-bd14-733eeba57b85.jpg)

## Technologies
-----------------------------------------------------------
Project is created with:
* Python version 3.12
* Flask\Django\FastAPI
* Modbus\M-Bus\Modbus-TCP

## Scheme
![image](https://user-images.githubusercontent.com/44020188/187191983-09bdd6a8-7a62-4bd9-ab2f-6382e4290327.png)


## Docker
-- Not Ready Yet --

## For code reviewer
Cześć Filip ! Na wejściu chaięłm podziękować że zechciałeś mi pomóc przy tym projekcie. W planach mam jeszcze kilka ciekawych pomysłów jak sklep internetowy (kolega sprzedaje ubrania przez Instagram, więc zaproponowałem mu że moglibyśmy stworzyć wspólnie jakiś WebSklepik), czy strona z cenami paliw na polskich stacjach ale to później ;)
Przygodę z programowaniem oraz IT zacząłem już w technikum (skończyłem technikum teleinformatyczne), tam z znajomymi tworzyliśmy pierwsze strony w PHP, oczywiście wszystko for fun i dla zabawy nic poważnego, niestety później porzyciłem temat na jakiś czas. Powórciłem do programowania jakieś 4 miesiące temu, zacząlem standardowo od poradników na YT, nastepnie kupiłem ksiażke "PYTHON Instrukcje dla programist" która naprawdę mocno pomogła w ogarnięciu oco chodzi. Przez jakiś czas jeszcze bawiłem się w wizualizację dany, Pandas, Matplotlib, ale czułem że to nie to. Potem sprubowałem trochę w girki korzystając z biblioteki PyGame, to już bardzoaj mi sie podobało, napewno sporo mi pomogło w zrozumieniu oco chodzi z OOP, aż wkońcu stanęło na tworzeniu stron. Od miesiąca trochę kręce się w miejcu, jak do niedawna sprawa była prosta bo wystarczyło klepać kod w Pythonie tak teraz gdy pojawiły się HTML/CSS/JS trochę mnie to przytłoczyło i utknąłem. Lekkie odetkanie nastapiło parę dni temu jak na paru grupkach napisałem posta "Hej kto chce coś robić razem ;) " i odziwo zgłosiło się trochę osób. Plan mam taki że z każdym z nich zrobię prosty projekt typu CRUD i zobacza kto co i ilę potrafi, a następnie podzielę na grupki. (Z tymi co zaczynają jakieś proste projetkty, a z tymi co już coś kumają jakieś większe projekty). Spokojnie nie będę Cię zalewał masą projektów z obcymi ludzimi ;) Ja to widze w ten sposób (Mogę się mylić bo dopiero zaczynam ). Na początku chciał bym sie skupić na tym projekcie, zobaczyć jak idzie współpraca (Wkońcu jest motywacja! bo ktoś patrzy mi się na ręce hahahha). Wiedzę którą Ty mi przekażesz ja postaram się przekazać tym osobą które faktycznie dopiero zaczynają, ucząc innych sami uczymy się szybciej, rzekomo. Raz jeszcze Thanks a lot! Cheers!


