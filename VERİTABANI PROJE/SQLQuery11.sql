use rentacar

CREATE TABLE KiralananAraclar(
aracmarka varchar(100),
aracmodel int,
aracplaka varchar(100) primary key,
arackm int,
kiralayanad varchar(100),
kiralayansoyad varchar(100),
gun int,
fiyat int
)

CREATE TABLE Araclar(
aracmarka varchar(100),
aracmodel int,
aracplaka varchar(50) primary key,
arackm int,
aracfiyat int
)


CREATE TABLE Sikayet(
sikayet varchar(500) primary key,
ad varchar(50),
soyad varchar(50)
)


CREATE TABLE Yonetici(
yoneticiadi varchar(100) primary key,
yoneticisoyadi varchar(100),
yoneticikulladi varchar(100),
yoneticisifre varchar(100),
yoneticiunvan varchar(100),
)


CREATE TABLE Kullanici(
kullaniciad varchar(100) primary key,
kullanicisoyad varchar(100),
kullanicikulladi varchar(100),
kullanicisifre varchar(100)
)





insert into Araclar values('Renault Talisman',2007,'16 TK 016',34247,5000)
insert into Araclar values('Mercedes CLA 200',2021,'23 AS 026',15000,3000)
insert into Araclar values('Porsche Taycan',2020,'34 CHV 123',24000,3000)






insert into KiralananAraclar values('Volvo S60',2023,'21 KK 234',70000,'Taþkýn','Kýþlak',2,2000)



insert into Kullanici values('Umut Emre','Karacaer','uekaracaer','uek123')
insert into Kullanici values('Taþkýn','Kýþlak','taskinkislak','taskin123')





insert into Sikayet values('Arabalar çok kirli !!!','Taþkýn','Kýþlak')
insert into Sikayet values('Arabanýn yaðý eksikti','Umut Emre','Karacaer')







CREATE TRIGGER t_araclar
ON Araclar
AFTER INSERT
AS
BEGIN
    DECLARE @arac_plaka VARCHAR(255) 

    SELECT @arac_plaka = aracplaka FROM INSERTED 

    IF EXISTS (SELECT aracplaka FROM Araclar WHERE aracplaka = @arac_plaka)
    BEGIN
        PRINT 'Plaka zaten mevcuttur.'
    END
END


CREATE TRIGGER KiralamaTrigger
ON KiralananAraclar
AFTER INSERT
AS
BEGIN
    DECLARE @aracplaka VARCHAR(100);
    DECLARE @gun INT;

    SET @aracplaka = (SELECT aracplaka FROM inserted);
    SET @gun = (SELECT gun FROM inserted);

    UPDATE KiralananAraclar
    SET arackm = arackm + @gun * 100
    WHERE aracplaka = @aracplaka;
END;




CREATE TRIGGER SikayetTrigger

ON Sikayet

AFTER INSERT

AS

BEGIN

PRINT('Þikayet Eklendi !')

END


CREATE TRIGGER YoneticiTrigger
ON Yonetici
AFTER INSERT
AS
BEGIN
    DECLARE @yoneticikulladi VARCHAR(100);
    DECLARE @yoneticisifre VARCHAR(100);

    SET @yoneticikulladi = (SELECT yoneticikulladi FROM inserted);
    SET @yoneticisifre = HASHBYTES('SHA2_512', @yoneticisifre);

    UPDATE Yonetici
    SET yoneticisifre = @yoneticisifre
    WHERE yoneticikulladi = @yoneticikulladi;
END;



CREATE TRIGGER KullaniciTrigger

ON Kullanici

AFTER INSERT
AS 
BEGIN

PRINT('Kullanýcý eklendi !')
END



