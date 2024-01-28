import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

#一括コメントアウトは ctrl + /
# 同じ文言を選択して操作したいときは ctrl + d

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!'

# expander
expander1 = st.expander('問い合わせ１')
expander1.write('問い合わせ１の内容を書く')
expander2 = st.expander('問い合わせ２')
expander2.write('問い合わせ２の内容を書く')
expander3 = st.expander('問い合わせ３')
expander3.write('問い合わせ３の内容を書く')


# st.write('Interactive Widgets')

# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')



# text = st.sidebar.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は', text ,'です。'

# condition = st.sidebar.slider('あなたの今の調子は？',0, 100, 50)
# 'コンディション : ', condition



# option = st.selectbox(
#         'あなたが好きな数字を教えてください',
#         list(range(1,11))
# )

# 'あなたの好きな数字は、', option ,'です。'

# st.write('Display Image')
# 
# if st.checkbox('Show Image'):
#     img = Image.open('image1.jpg')
#     st.image(img, caption='Eto_2024', use_column_width=True)

audio_file = open('vigilante.wav','rb')
st.audio(audio_file, format="audio/wav", start_time=0)




# st.write('DataFrame')

# ★マップ

# df = pd.DataFrame(
#     np.random.rand(100, 2)/(50, 50) + (34.88, 135.41),
#     columns=['lat', 'lon']
# )
# st.map(df)

# ★チャート

#df = pd.DataFrame(
#    np.random.rand(20, 3),
#    columns=['a', 'b', 'c']
#)
#
#st.line_chart(df)
#st.area_chart(df)

# ★表

#  動的 st.write(df)
#　動的、拡張 st.dataframe(df.style.highlight_max(axis=0) , width=200, height=200)
#　静的、st.table(df.style.highlight_max(axis=0))

# ★マジックコマンド

# """
# # 章
# ## 節
# ### 項
# 
# ``` python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# チャートを描く

