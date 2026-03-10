import time
list=[]
print("görev listesi yükleniyor...")
time.sleep(1.2)
print("aşağıdaki numaralardan birini seçiniz")

#burada önce bir liste oluşturuyoruz.
seçenekler=["görev ekle","görevleri göster","görev sil","çıkış yap"]

#burada, oluşturduğumuz listeyi numaralandırıp alt alta yazdırıyoruz.
#enumerate fonksiyonunu ise hem listeyi numaralandırmak hem de alt alta yazdırmak yani 2'li paketler oluşturmak için kullanıyoruz.
for i,seçenekler in enumerate(seçenekler,1):
  print(f"{i}={seçenekler}")

#burada, kullanıcılardan alınan seçimlere göre işlem yapmak için bir döngü oluşturuyoruz=while döngüsü.
while True:

  #try bloğu,kullanıcıların rakam dışında bir tuşlama yapması halinde programın hata vermesini önler yani süspansiyon görevi görür.
  try:
    
    #int fonksiyonu, kullanıcının girdiği veriyi tam sayıya çevirir.
    seçim=int(input("\nseçiminizi giriniz:  örn:1. "))
    if seçim>4 or seçim<=0:
      print("\nlütfen 1-4 arası bir rakam tuşlayınız!")
      
    elif seçim== 1:
      görev_ekle=input("\ngörev ekle:")
      #append fonksiyonu, kullanıcının girdiği veriyi listeye ekler.
      list.append(görev_ekle)
      
    elif seçim== 2:
      print("\neklenen görevler:")
      for i,görev_göster in enumerate(list,start=1):
        print(f"{i}.{görev_göster}")
        
    elif seçim== 3:
      görev_sil=int(input("\nsilmek istediğiniz görev numarasını giriniz:"))
      #pop fonksiyonu, kullanıcının girdiği numaradaki görevi listeden siler.
      list.pop(görev_sil-1)
      print(f"\n{görev_sil} görevi silindi.")
      print("yeni liste:",list)#buradaki list'i sil ve printin altına bir for döngüsü oluştur ve listeyi alt alta yazdır.
      
    elif seçim==4:
      print("çıkış yapılıyor...")
      time.sleep(2)
      #break komutu, döngüyü sonlandırır. bu sayede çıkış yapma komutunu oluştururuz.
      break
      
  #except bloğu, kullanıcının rakam dışında bir tuşlama yapması halinde programın hata vermesini önleyerek kullanıcıya uyarı verir.    
  except:
    print("\nseçiminiz yalnızca rakam olmalıdır!")