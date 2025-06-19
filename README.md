# LangChainWorkSpace

Bu proje, LinkedIn profillerinden veri çekmek ve bu verilerle sohbet başlatıcı (ice breaker) öneriler üretmek için geliştirilmiştir. Proje, çeşitli ajanlar ve araçlar kullanarak LinkedIn API'si ile etkileşime geçer.

---

This project is designed to fetch data from LinkedIn profiles and generate ice breaker suggestions using that data. It interacts with the LinkedIn API via various agents and tools.

## Klasör Yapısı / Project Structure

- `agents/`: LinkedIn verilerini işleyen ve yöneten ajanlar / Agents for processing LinkedIn data.
- `third_parties/`: LinkedIn gibi üçüncü parti servislerle entegrasyon kodları / Integrations with third-party services like LinkedIn.
- `tools/`: Projede kullanılan yardımcı araçlar / Utility tools used in the project.
- `ice_breaker.py`: Ana uygulama dosyası / Main application script.

## Kurulum / Installation

1. Depoyu klonlayın / Clone the repository:
   ```bash
   git clone <https://github.com/burakKocabas03/LangChainWorkSpace/tree/1-start-here>
   cd LangChainWorkSpace
   ```

2. Gerekli paketleri yükleyin / Install dependencies:
   ```bash
   pip install pipenv
   pipenv install
   ```

3. Ortamı başlatın / Activate the environment:
   ```bash
   pipenv shell
   ```

## Kullanım / Usage

Ana scripti çalıştırmak için / To run the main script:
```bash
python ice_breaker.py
```

## Katkıda Bulunma / Contributing

Pull request'ler kabul edilir. Lütfen önce bir issue açın. / Pull requests are welcome. Please open an issue first.

## Lisans / License

MIT