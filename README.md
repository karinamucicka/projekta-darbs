# Projekta darbs

### Projekta uzdevums

Šī projekta uzdevums ir izveidot Python codu, kas veic tīmekļa datu ieguvi (web scraping) no futbola statistikas vietnes, lai iegūtu informāciju par futbola spēlēm, tostarp datumu, komandu nosaukumus un rezultātus. Projekta galvenais mērķis ir izveidot automatizētu datu ieguves programmatūru, kas sniedz iespēju iegūt un organizēt informāciju no dotās interneta vietnes(https://www.adamchoi.co.uk/corners/detailed) un ērti apkopot iegūtos datus, saglabājot tos CSV failā, lai tos būtu viegli izmantot turpmākai analīzei un aplūkošanai.

### Bibliotēku iznamtošana

Selenium- Selenium ir automācijas rīks, kas tiek izmantots galvenokārt tīmekļa pārlūku testēšanai, bet tas ir noderīgs arī datu ieguvei un darbību automatizēšanai tīmeklī. Selenium ļauj automatizēt pārlūku darbības, piemēram, lapu atvēršanu, pogu nospiešanu, teksta ievadīšanu u.t.t. Ar Selenium var arī automātiski iegūt informāciju no tīmekļa vietnēm, izmantojot tīmekļa lapu elementu atlasīšanu un datu izgūšanu. Šajā projektā Selenium tiek izmantots, lai automatizētu darbību ar futbola statistikas vietni, piemēram, atvērtu vietni, uzspiestu uz pogas 'All Matches' un izvadītu futbola rezultātu statistiku.

Pandas- Pandas ir efektīva datu analīzes bibliotēka Python vidē. Tā nodrošina struktūras piemēram DataFrame, lai ērti organizētu un analizētu datus. Šajā projektā futbola statistikas dati tiks organizēti un pārvaldīti ar Pandas bibliotēkas palīdzību. Pandas bibliotēka tika izvēlēta, jo ā ir viegli pielietojama, taču ļoti efektīva.Es izmantoju Pandas DataFrame, kas nodrošina ērtu veidu kā strādāt ar tabulas veida datiem, ļaujot tos viegli analizēt un vizualizēt.

### Izmantotās metodes un vispārējs koda apraksts

**1.Bibliotēku isntalācija un importēšana**

Pirms koda veidošanas jāpārliecinās par to, vai bibliotēkas Selenium un Pandas ir ieinstalētas.
Lai ieinstalētu bibliotēkas, ir nepieciešams ierakstīt terminālī sekojošās komandas: pip install selenium, pip isntall pandas

**2.Selenium Webdriver inicializācija**

Kods sākas ar bibliotēku importēšanu un Selenium Webdriver inicializāciju, izmantojot Chrome pārlūku:

    import selenium
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import pandas as pd
    driver = webdriver.Chrome()

 Šis solis nodrošina iespēju automatizēt pārlūka darbības.

 **3.Tīmekļa vietnes apmeklēšana**

 Tīmekļa vietnes atvēršanai un apmeklēšanai ir nepieciešams ievadīt nepieciešamo linku (url) un izmantot ''get'' metodi:

     url="https://www.adamchoi.co.uk/corners/detailed"
     driver.get(url)

**4. Pogas ''All matches'' piespiešana**

''All matches'' pogas piespiešanai tiek izmantots XPath. Izmantojot XPath, var precīzi norādīt, kuri HTML elementi ir nepieciešami uzdevuma veikšanai. Lai iegūtu XPath ir nepieciešam manuāli apmeklēt vietni, uzspiest uz labā taustiņa un izvēlēties opciju ''inspect''. Tiks atvērti visi HTML dati, kuros var atrast visus sev nepieciešamos datus ar XPath. Lai izveidotu XPath ir jauzspiež Ctrl+F un jāatrod un jaievada nepieciešamā informācija izmantojot vairākas metodes: 

>//- atrod visus elementus neatkarīgi no tā, kur tie atrodas

>/- atrod elementus tieši zem esošā elementa

>[]- filtrē elementus, piemēram, [1] atradīs pirmo elementu

>@- atsaucas uz elementa atribūtiem, piemēram, @class

>text()- atsaucas uz elementa tekstu

Kad XPath ir iegūts, tas tiek ievietots metodē ''find_element'' ar kura palīdzību tiek atrasti dati:

>[!TIP]
>Ja nepieciešams atrast vairākus elementus, tad jāizmanto ''find_elements''

    all_matches_button= driver.find_element(By.XPATH, value='//label[@analytics-event="All matches"]')

Tad ar komandas ''click'' palīdzību programma pati uzspiež uz ''All matches'' pogu:

    all_matches_button.click()

**5. Tabulas rindu iegūšana**

''find_elements'' metode atrod visas tabulas rindas, kuras ir marķētas ar 'tr' HTML tagu.

    tables= driver.find_elements(By.TAG_NAME, value='tr')

**6. Datu iegūšana no katras rindas**

Sākumā tiek izveidota vieta jeb saraksts, kur iegūtos datus glabās, piemēram:

    home_team=[]

Tad tiek veikta iterācija caur katru tabulas rindu un no katras rindas tiek iegūti dati par datumiem, komandām un rezultātiem, izmantojot atbilstošos XPaths:

    for table in tables:
        date.append(table.find_element(By.XPATH, value='/td[1]').text)
        home_team.append(table.find_element(By.XPATH, value='/td[2]').text)
        score.append(table.find_element(By.XPATH, value='/td[3]').text)
        away_team.append(table.find_element(By.XPATH, value='/td[4]').text)

**7. WebDriver aizvēršana**

Kad visi nepieciešamie dati ir izvilkti no tīmekļa vietnes, ir nepieciešams aizvērt Chrome WebDriver ar metodi ''quit''

    driver.quit()

**8.Datu organizēšana ar Pandas**

Šī koda daļa izmanto Pandas, lai izveidotu DataFrame, kas ir divdimensionāla tabulveida datu struktūra. Lai izveidotu jaunu DataFrame ir jāizmanto komanda ''DataFrame''. Ikšpus komandā ir jāievieto {}, kurās jāievada kollonas nosaukums un sarakstus, kuros ir ievieti nepieciešamie dati.

    dataframe=pd.DataFrame({'date':date, 'home team':home_team,'score':score, 'away team':away_team})

**9. Datu pārvietošana uz CSV failu**

Lai pārvietotu iegūtos datus, kuri ir saglabāti mainīgajā dataframe, CSV failā šim mainīgajam ir jāpievieno komanda ''to_csv'' un jānorāda vēlamais faila nosaukums.

    dataframe.to_csv('football_data.csv')


### Papildinājumi

Projekts ir pielāgojams papildināšanai, piemēram, pievienojot funkcionalitāti automātiskai datu atjaunošanai. Kā arī var papildināt analizējot csv datus konkrētāk, izvēloties precīzus datumus vai komandas. Ir iespējams papildināt kodu ar vairāk informāciju, piemēram, vairākām valstī vai pat vairākiem sporta veidiem.

### Secinājumi

Projekts izdevās, es ieguvu nepieciešamo informāciju un tā bija pareiza. Projekts par futbola statistikas datu ieguvi ir labs piemērs tam, kā izmantot Python programmatūru ar Selenium bibliotēku, lai automatizētu datu ieguvi un analīzi no tīmekļa vietnēm. Šis kods var palīdzēt ikdienā, jo to var izmantot atkārtoti un ir iespējams papildināt kodu, lai izgūtu vēl precīzāku informāciju no CSV faila.

