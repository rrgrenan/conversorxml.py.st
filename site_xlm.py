import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET
import io


st.set_page_config(page_title="Conversor NF-e", layout="centered")

# Assinatura no topo
st.markdown("<h1 style='text-align: right; line-height: 1.2;'>Renan<br>Gonçalves</h1>", unsafe_allow_html=True)


st.title("📄 Conversor de Nota Fiscal Eletrônica (XML → Excel)")

uploaded_file = st.file_uploader("Envie o arquivo XML da NF-e", type=["xml"])

def processar_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    ns = {'ns': root.tag.split('}')[0].strip('{')} if '}' in root.tag else {}

    itens = []
    for det in root.findall('.//ns:det', ns) if ns else root.findall('.//det'):
        nItem = det.attrib.get('nItem')
        prod = det.find('ns:prod', ns) if ns else det.find('prod')
        imposto = det.find('ns:imposto', ns) if ns else det.find('imposto')

        item = {
            'nItem': nItem,
            'cProd': prod.findtext('ns:cProd', namespaces=ns) if ns else prod.findtext('cProd'),
            'cEAN': prod.findtext('ns:cEAN', namespaces=ns) if ns else prod.findtext('cEAN'),
            'xProd': prod.findtext('ns:xProd', namespaces=ns) if ns else prod.findtext('xProd'),
            'qCom': prod.findtext('ns:qCom', namespaces=ns) if ns else prod.findtext('qCom'),
            'vUnCom': prod.findtext('ns:vUnCom', namespaces=ns) if ns else prod.findtext('vUnCom'),
            'vProd': prod.findtext('ns:vProd', namespaces=ns) if ns else prod.findtext('vProd'),
            'NCM': prod.findtext('ns:NCM', namespaces=ns) if ns else prod.findtext('NCM'),
            'CEST': prod.findtext('ns:CEST', namespaces=ns) if ns else prod.findtext('CEST'),
            'CFOP': prod.findtext('ns:CFOP', namespaces=ns) if ns else prod.findtext('CFOP'),
            'ICMS': imposto.findtext('.//ns:vICMS', namespaces=ns) if ns else imposto.findtext('.//vICMS'),
            'PIS': imposto.findtext('.//ns:vPIS', namespaces=ns) if ns else imposto.findtext('.//vPIS'),
            'COFINS': imposto.findtext('.//ns:vCOFINS', namespaces=ns) if ns else imposto.findtext('.//vCOFINS'),
        }

        itens.append(item)

    df = pd.DataFrame(itens)
    return df

if uploaded_file:
    with st.spinner("Processando XML..."):
        try:
            df = processar_xml(uploaded_file)
            st.success("✅ Nota processada com sucesso!")
            st.dataframe(df)

            buffer = io.BytesIO()
            df.to_excel(buffer, index=False, engine='openpyxl')
            buffer.seek(0)

            st.download_button(
                label="📥 Baixar Excel",
                data=buffer,
                file_name="nota_convertida.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {e}")
