import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the pre-trained model
model = joblib.load(r"C:\Users\noagb\OneDrive\Masaüstü\final sunum\Deneme 2\project\predict_model_v2.joblib")

# Prepare label encoders
data = pd.DataFrame({
    'person_home_ownership': ['OWN', 'MORTGAGE', 'RENT', 'OTHER', 'OWN' , 'OTHER', 'OWN'],
    'loan_intent': ['EDUCATION', 'DEBTCONSOLIDATION', 'VENTURE', 'MEDICAL' , 'PERSONAL', 'HOMEIMPROVEMENT' , 'HOMEIMPROVEMENT' ],
    'loan_grade': ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G'],
    'cb_person_default_on_file': ['Y', 'N', 'N', 'N', 'Y' ,'N' , 'Y']
})

categorical_variables = ['person_home_ownership', 'loan_intent', 'loan_grade', 'cb_person_default_on_file']
label_encoders = {}

for col in categorical_variables:
    label_encoders[col] = LabelEncoder()
    data[col] = label_encoders[col].fit_transform(data[col])

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton button {
        background-color: #007BFF;
        color: white;
        border-radius: 5px;
    }
    .stNumberInput input, .stSelectbox div {
        border-radius: 5px;
        border: none;
        box-shadow: none;
        padding: 5px;
    }
    .stNumberInput label, .stSelectbox label {
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Main app
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Ana Sayfa", "Ürünlerimiz", "Hizmetlerimiz", "Fiyatlarımız", "Kredi Durumu Hesaplama", "Sıkça Sorulan Sorular", "İletişim"])

with tab1:
    st.title("Bankacılık Uygulamasına Hoş Geldiniz")
    st.image(r"C:\Users\noagb\OneDrive\Masaüstü\kredi reklam.png", use_column_width=True)
    
    st.header("En Uygun Kredi Fırsatları")
    st.markdown("""
        - **Konut Kredisi:** Düşük faiz oranları ile hayalinizdeki eve sahip olun.
        - **İhtiyaç Kredisi:** Anında onay ile nakit ihtiyaçlarınızı karşılayın.
        - **Taşıt Kredisi:** Uygun ödeme koşulları ile yeni aracınıza kavuşun.
    """)
    st.image(r"C:\Users\noagb\OneDrive\Masaüstü\20854817_s-1.png", use_column_width=True)
    
    st.header("Güncel Haberler")
    st.markdown("""
        - **Bankamızdan Yeni Hizmet:** Artık tüm kredi kartı işlemlerinizi mobil uygulamamız üzerinden gerçekleştirebilirsiniz.
        - **Yatırım Fırsatları:** Yeni yatırım danışmanlığı hizmetlerimizle birikimlerinizi güvenle değerlendirin.
    """)

with tab2:
    st.title("Ürünlerimiz")
    st.markdown("""
        - **Konut Kredisi:** Düşük faiz oranları ile hayalinizdeki eve sahip olun.
        - **İhtiyaç Kredisi:** Anında onay ile nakit ihtiyaçlarınızı karşılayın.
        - **Taşıt Kredisi:** Uygun ödeme koşulları ile yeni aracınıza kavuşun.
        - **Kredi Kartları:** Size özel avantajlarla dolu kredi kartlarımızı keşfedin.
        - **Eğitim Kredileri:** Geleceğinize yatırım yapın, düşük faiz oranları ile eğitim kredisi alın.
    """)

with tab3:
    st.title("Hizmetlerimiz")
    st.markdown("""
        - **Online Bankacılık:** Hızlı ve güvenli bankacılık işlemleri.
        - **Yatırım Danışmanlığı:** Uzman kadromuzla doğru yatırım kararları alın.
        - **Sigorta Hizmetleri:** Hayatınızı ve geleceğinizi güvence altına alın.
        - **Kredi Kartları:** Size özel avantajlarla dolu kredi kartlarımızı keşfedin.
        - **Eğitim Kredileri:** Geleceğinize yatırım yapın, düşük faiz oranları ile eğitim kredisi alın.
    """)

with tab4:
    st.title("Fiyatlarımız")
    st.markdown("""
        - **Konut Kredisi:** %1.20 faiz oranı
        - **İhtiyaç Kredisi:** %1.50 faiz oranı
        - **Taşıt Kredisi:** %1.30 faiz oranı
        - **Eğitim Kredisi:** %1.10 faiz oranı
    """)

with tab5:
    st.title("Kredi Durumu Hesaplama")
    st.markdown("Bankamızın kredi riski değerlendirme aracına hoş geldiniz. Lütfen aşağıdaki formu doldurarak kredi uygunluğunuzu öğrenin.")

    # Input fields for user data
    st.header("Kişisel Bilgiler")
    person_age = st.number_input("Kişi Yaşı", min_value=18, max_value=100, value=21)
    person_income = st.number_input("Kişi Geliri", min_value=0, value=1600)
    person_home_ownership = st.selectbox("Konut Sahipliği Durumu", options=label_encoders['person_home_ownership'].classes_)
    person_emp_length = st.number_input("İş Süresi (Yıl)", min_value=0.0, value=5.0)

    st.header("Kredi Bilgileri")
    loan_intent = st.selectbox("Kredi Amacı", options=label_encoders['loan_intent'].classes_)
    loan_grade = st.selectbox("Kredi Derecesi", options=label_encoders['loan_grade'].classes_)
    loan_amnt = st.number_input("Kredi Miktarı", min_value=0, value=106600)
    loan_int_rate = st.number_input("Kredi Faiz Oranı", min_value=0.0, max_value=100.0, value=11.14)
    loan_percent_income = st.number_input("Kredi/Gelir Oranı", min_value=0.0, max_value=1.0, value=0.1)

    st.header("Kredi Geçmişi")
    cb_person_default_on_file = st.selectbox("Kredi Bürosu: Kişinin Temerrüt Durumu", options=label_encoders['cb_person_default_on_file'].classes_)
    cb_person_cred_hist_length = st.number_input("Kredi Geçmişi Süresi", min_value=0, value=2)

    # Button to trigger prediction
    if st.button("Tahmin Et"):
        input_data = pd.DataFrame({
            'person_age': [person_age],
            'person_income': [person_income],
            'person_home_ownership': [person_home_ownership],
            'person_emp_length': [person_emp_length],
            'loan_intent': [loan_intent],
            'loan_grade': [loan_grade],
            'loan_amnt': [loan_amnt],
            'loan_int_rate': [loan_int_rate],
            'loan_percent_income': [loan_percent_income],
            'cb_person_default_on_file': [cb_person_default_on_file],
            'cb_person_cred_hist_length': [cb_person_cred_hist_length]
        })

        for col in categorical_variables:
            input_data[col] = label_encoders[col].transform(input_data[col])

        input_data["Yaş/Gelir Oranı"] = input_data["person_age"] / input_data["person_income"]
        input_data['Kredi Miktarı/Yaş Oranı'] = input_data["loan_amnt"] / input_data["person_age"]
        input_data['Kredi Oranı'] = (input_data["loan_amnt"] * input_data['loan_int_rate']) / input_data['person_income']
        input_data["Derece/Kredi Miktarı Oranı"] = input_data["loan_grade"] / input_data["loan_amnt"]

        # Make prediction
        prediction = model.predict(input_data)
        prediction_text = 'Uygun' if prediction[0] == 1 else 'Uygun Değil'

        # Display prediction
        st.subheader(f"Kredi Durumu: {prediction_text}")
        st.markdown("Kredi riski değerlendirme aracımızı kullandığınız için teşekkür ederiz.")

with tab6:
    st.title("Sıkça Sorulan Sorular")
    st.markdown("""
        **Kredi başvuru süresi ne kadar sürer?**
        Kredi başvuruları genellikle 1-2 iş günü içinde sonuçlanır.
        
        **Hangi belgeler gereklidir?**
        Kredi başvurusu için kimlik, gelir belgesi ve ikametgah belgesi gereklidir.
        
        **Faiz oranlarınız nedir?**
        Faiz oranlarımız kredi türüne ve başvuranın kredi notuna göre değişmektedir.
        
        **Online bankacılık güvenli midir?**
        Evet, bankamızın online bankacılık sistemi en son güvenlik protokolleri ile korunmaktadır.
    """)

with tab7:
    st.title("İletişim")
    st.markdown("""
        **Adres:** 123 Banka Caddesi, Finans Şehri, Ülke
        **Telefon:** +90 123 456 7890
        **Email:** info@yourbank.com
        **Çalışma Saatleri:** Pazartesi-Cuma, 09:00 - 18:00
    """)
