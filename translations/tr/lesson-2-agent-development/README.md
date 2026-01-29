# Ders 2 Ajan Geliştirme

"Yapay Zeka Ajanını Sıfırdan Üretime İnşa Etme Kursu"nun ikinci dersine hoş geldiniz!

Bu derste şunları ele alacağız:

- Yapay Zeka Ajanlarımızı Oluşturmak İçin Kullanacağımız Araçlar
  
- Geliştirme Kaynaklarımız İçin Kurulum Talimatları

- Yapay Zeka Ajanı Geliştirme En İyi Uygulamaları
  
- Yapay Zeka Ajanlarımızı Oluşturmak İçin Kod İncelemesi
  
Yapay Zeka Ajanlarımızı oluşturmak için kullanacağımız araçlara bakarak başlayalım.

## Araçlar ve Kurulum Talimatları

### Microsoft Foundry

Büyük Dil Modellerine (LLM'lere) erişim için [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) kullanacağız. Foundry kullanmanın maliyetleri vardır, bu yüzden hâlihazırda erişiminiz yoksa lütfen hesap kurulumu için verilen talimatları takip ettiğinizden emin olun.

### OpenAI Modelleri

Bu kurstaki ajan kod örnekleri, OpenAI modellerini [Microsoft Foundry](https://azure.microsoft.com/products/ai-foundry) üzerinden kullanacak şekilde ayarlanmıştır.

Bir modeli Foundry kullanarak nasıl dağıtacağınızı öğrenmek için bu kılavuzu kullanın: [Foundry portalında Microsoft Foundry Modellerini Dağıtma](https://learn.microsoft.com/azure/ai-foundry/foundry-models/how-to/deploy-foundry-models?view=foundry-classic)

Bu kurs için GPT-4.1 veya daha yeni bir modeli seçin.

### Microsoft Agent Framework

Daha önce belirtildiği gibi, Yapay Zeka Ajanlarımızı oluşturmak ve düzenlemek için [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) kullanacağız.

Microsoft Agent Framework ve diğer gerekli paketleri yüklemek için, bu projenin kök dizinindeyken aşağıdaki komutu çalıştırın:

```bash
pip install -r requirements.txt
```

### .env Değişkenlerini Kurma

Bu kurstaki kod örneklerini çalıştırmak için, bu projenin kök dizininde bir `.env` dosyası oluşturmanız gerekecek.

Kolaylık olması için, verilen `.env.example` dosyasını kopyalayabilirsiniz:

```bash
cp .env.example .env
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, yapay zeka çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi diliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımı sonucunda oluşabilecek herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->