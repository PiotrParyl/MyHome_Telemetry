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
Cze???? Filip ! Na wej??ciu chai????m podzi??kowa?? ??e zechcia??e?? mi pom??c przy tym projekcie. W planach mam jeszcze kilka ciekawych pomys????w jak sklep internetowy (kolega sprzedaje ubrania przez Instagram, wi??c zaproponowa??em mu ??e mogliby??my stworzy?? wsp??lnie jaki?? WebSklepik), czy strona z cenami paliw na polskich stacjach ale to p????niej ;)
Przygod?? z programowaniem oraz IT zacz????em ju?? w technikum (sko??czy??em technikum teleinformatyczne), tam z znajomymi tworzyli??my pierwsze strony w PHP, oczywi??cie wszystko for fun i dla zabawy nic powa??nego, niestety p????niej porzyci??em temat na jaki?? czas. Pow??rci??em do programowania jakie?? 4 miesi??ce temu, zacz??lem standardowo od poradnik??w na YT, nastepnie kupi??em ksia??ke "PYTHON Instrukcje dla programist" kt??ra naprawd?? mocno pomog??a w ogarni??ciu oco chodzi. Przez jaki?? czas jeszcze bawi??em si?? w wizualizacj?? dany, Pandas, Matplotlib, ale czu??em ??e to nie to. Potem sprubowa??em troch?? w girki korzystaj??c z biblioteki PyGame, to ju?? bardzoaj mi sie podoba??o, napewno sporo mi pomog??o w zrozumieniu oco chodzi z OOP, a?? wko??cu stan????o na tworzeniu stron. Od miesi??ca troch?? kr??ce si?? w miejcu, jak do niedawna sprawa by??a prosta bo wystarczy??o klepa?? kod w Pythonie tak teraz gdy pojawi??y si?? HTML/CSS/JS troch?? mnie to przyt??oczy??o i utkn????em. Lekkie odetkanie nastapi??o par?? dni temu jak na paru grupkach napisa??em posta "Hej kto chce co?? robi?? razem ;) " i odziwo zg??osi??o si?? troch?? os??b. Plan mam taki ??e z ka??dym z nich zrobi?? prosty projekt typu CRUD i zobacza kto co i il?? potrafi, a nast??pnie podziel?? na grupki. (Z tymi co zaczynaj?? jakie?? proste projetkty, a z tymi co ju?? co?? kumaj?? jakie?? wi??ksze projekty). Spokojnie nie b??d?? Ci?? zalewa?? mas?? projekt??w z obcymi ludzimi ;) Ja to widze w ten spos??b (Mog?? si?? myli?? bo dopiero zaczynam ). Na pocz??tku chcia?? bym sie skupi?? na tym projekcie, zobaczy?? jak idzie wsp????praca (Wko??cu jest motywacja! bo kto?? patrzy mi si?? na r??ce hahahha). Wiedz?? kt??r?? Ty mi przeka??esz ja postaram si?? przekaza?? tym osob?? kt??re faktycznie dopiero zaczynaj??, ucz??c innych sami uczymy si?? szybciej, rzekomo. Raz jeszcze Thanks a lot! Cheers!


