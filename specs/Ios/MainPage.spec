Specification Heading
=====================
Created by testinium on 31.07.2023

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
IOS Scenario Main Page Campaign Swipe And Click
-----------------------------------------------
tags:Gratis_IOS_AnasayfaKampanyalarSwipeVeTiklama
* Uygulama baslatilir
* Kampanyalar swipe edilir
* Kampanyaya tiklanir
//* En Cok Satanlar basliklari swipe edilir ve tiklanir
* En Cok Satanlar urunleri swipe edilir ve tiklanir
* Ana sayfa kampanyalarina tiklanir
* En Son Gezdiklerim urunleri swipe edilir ve tiklanir

IOS Scenario Non-Login Add Favorite
-----------------------------------
tags:Gratis_IOS_AnasayfaNonLoginFavoriEkleme
* Uygulama baslatilir
* En Cok Satanlar alanindan bir urunun favori butonuna tıklanir
* Yeni favori ikonu ile Gratis0 login olunur
* Urun favorilere eklenir
* Favori listesi kontrol edilerek temizlenir

IOS Scenario Non-Login Add Favorite List
----------------------------------------
tags:Gratis_IOS_NonLoginFavoriListesiOlusturma
* Uygulama baslatilir
* En Cok Satanlar alanindan bir urunun favori butonuna tıklanir
* Yeni favori ikonu ile Gratis1 login olunur
* Yeni favori listesi olusturulur ve secilen urun favori eklenir
* Diger'e tiklanir diger sayfasinin acildigi gorulur
* Profil'e tiklanir profilim sayfasinin acildigi gorulur
* Profil sayfasındaki Favorilerim ikonuna tiklanir
* Listeden yeni eklenen favori listesi secilir
* Favori listesi silinir

IOS Scenario Non-Login Add To Cart
----------------------------------
tags:Gratis_IOS_NonLoginSepeteEkleme
* Uygulama baslatilir
* Non-Login ana sayfadan bir urun sepete eklenir
* Yeni Sepete Ekle butonu ile Gratis2 login olunur
* Alışverişe devam edilir
* Uygulamadan cikis yapilir
* Ana sayfa tab'ına tıklanır
* Non-Login ana sayfadan bir urun sepete eklenir
* Yeni Sepete Ekle butonu ile Gratis5 login olunur
* Sepete git'e tıklanır
* Sepet kasa arkasi popup'i kapatilir
* Sepet kontrol edilerek temizlenir

IOS Scenario Visited Add Favorite
---------------------------------
tags:Gratis_IOS_EnSonGezdiklerimFavori
* Uygulama baslatilir
* Yeni login sayfasina gecilir
* Yeni Gratis3 ile login olunur
* Ana sayfa tab'ına tıklanır
* En Çok Satanlar ürünlerine tıklanır
* En Son Gezdiklerim alanına gidilir
* En Son Gezdiklerim alanından bir ürünün favori butonuna tıklanır
* Urun favorilere eklenir
* Ana sayfadaki urun favorilerden cikarilir
* En Son Gezdiklerim alanından bir ürünün favori butonuna tıklanır
* Yeni favori listesi olusturulur ve secilen urun favori eklenir
* Diger'e tiklanir diger sayfasinin acildigi gorulur
* Profil'e tiklanir profilim sayfasinin acildigi gorulur
* Profil sayfasındaki Favori butonuna tiklanir
* Listeden yeni eklenen favori listesi secilir
* Favori listesi silinir

IOS Scenario Non-Login Visited Add Favorite
-------------------------------------------
tags:Gratis_IOS_NonLoginEnSonGezdiklerimFavori
* Uygulama baslatilir
* En Çok Satanlar ürünlerine tıklanır
* En Son Gezdiklerim alanına gidilir
* En Son Gezdiklerim alanından bir ürünün favori butonuna tıklanır
* Yeni favori ikonu ile Gratis1 login olunur
* Urun favorilere eklenir
* Ana sayfadaki urun favorilerden cikarilir
* Uygulamadan cikis yapilir
* Ana sayfa tab'ına tıklanır
* En Son Gezdiklerim alanından bir ürünün favori butonuna tıklanır
* Yeni favori ikonu ile Gratis5 login olunur
* Yeni favori listesi olusturulur ve secilen urun favori eklenir
* Diger'e tiklanir diger sayfasinin acildigi gorulur
* "1" kere yukarı doğru kaydır
* Profil'e tiklanir profilim sayfasinin acildigi gorulur
* Profil sayfasındaki Favori butonuna tiklanir
* Listeden yeni eklenen favori listesi secilir
* Favori listesi silinir

IOS Scenario Visited Add To Cart
--------------------------------
tags:Gratis_IOS_EnSonGezdiklerimSepet
* Uygulama baslatilir
* Yeni login sayfasina gecilir
* Yeni Gratis2 ile login olunur
* Ana sayfa tab'ına tıklanır
* En Çok Satanlar ürünlerine tıklanır
* En Son Gezdiklerim alanına gidilir
* En Son Gezdiklerim alanından bir ürünün sepet butonuna tiklanir
* Alışverişe devam edilir
* En Son Gezdiklerim alanından bir ürünün sepet butonuna tiklanir
* Sepete git'e tıklanır
* Sepet kasa arkasi popup'i kapatilir
* Sepet kontrol edilerek temizlenir

IOS Scenario Non-Login Visited Add To Cart
------------------------------------------
tags:Gratis_IOS_EnSonGezdiklerimNonLoginSepetDevam
* Uygulama baslatilir
* En Çok Satanlar ürünlerine tıklanır
* En Son Gezdiklerim alanına gidilir
* En Son Gezdiklerim alanından bir ürünün sepet butonuna tiklanir
* Yeni Sepete Ekle butonu ile Gratis3 login olunur
* Alışverişe devam edilir

IOS Scenario Non-Login Visited Add To Cart And Go To Cart
---------------------------------------------------------
tags:Gratis_IOS_EnSonGezdiklerimNonLoginSepeteGit
* Uygulama baslatilir
* En Çok Satanlar ürünlerine tıklanır
* En Son Gezdiklerim alanına gidilir
* En Son Gezdiklerim alanından bir ürünün sepet butonuna tiklanir
* Yeni Sepete Ekle butonu ile Gratis4 login olunur
* Sepete git'e tıklanır
* Sepet kasa arkasi popup'i kapatilir
* Sepet kontrol edilerek temizlenir

BasicIOSTesti
-----
tags:Basic_IOSTesti
* Uygulama baslatilir
* "2" saniye bekle
* "gratisBosBtn" li element varsa tıkla

Success01
-----
tags:Success01
*Uygulama baslatilir
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle

Success02
-----
tags:Success02
*Uygulama baslatilir
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle

Success03
-----
tags:Success03
*Uygulama baslatilir
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle

Success04
-----
tags:Success04
*Uygulama baslatilir
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle

Success05
-----
tags:Success05
*Uygulama baslatilir
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle

Success06
-----
tags:Success06
*Uygulama baslatilir
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle

Success07
-----
tags:Success07
*Uygulama baslatilir
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle

Success08
-----
tags:Success08
*Uygulama baslatilir
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle

Success09
-----
tags:Success09
*Uygulama baslatilir
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle

Success10
-----
tags:Success10
*Uygulama baslatilir
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle

BasicIOSFail
-----
tags:Basic_IOSFail
*Uygulama baslatilir
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "markalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kategorilerSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesi" li element varsa tıkla
* "2" saniye bekle
* "kampanyalarSekmesilllllll" li element varsa tıkla
