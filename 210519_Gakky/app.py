# -*- coding: utf-8 -*-
import streamlit as st
import datetime

dt_now = datetime.datetime.now()

st.title('Cloud Gakky')
your_name = st.text_input("ガッキーと結婚するのは・・・？", "星野源")
text_1 = your_name + "・新垣結衣　連名コメント"
text_2 = "私たち、" + your_name + "・新垣結衣は、このたび結婚する運びとなりました事をご報告させて いただきます。"
text_3 = your_name + "  　新垣結衣"
'''
***
'''
st.write(text_1)
st.write("関係者の皆様")
st.write("新緑の候、皆様におかれましてはご清栄のこととお慶び申し上げます。")
st.write("平素は格別のご高配を賜り、厚く御礼申し上げます。")
st.write(text_2)
st.write("これからも互いに支え合い豊かな時間を積み重ねていけたらと思っております。 未熟な二人ではございますが、温かく見守っていただけますと幸いです。 今後ともご指導ご鞭撻を賜りますようお願い申し上げます。")
st.write("最後になりますが、新型コロナウイルスの感染拡大が1日でも早く終息する事を、心よりお祈り申し上げます。")
st.write(dt_now.strftime('%Y年%m月%d日'))
st.write(text_3)
'''
***
'''
agree = st.checkbox('現実ボタン')

if agree == True :
     st.write('星野源さん、新垣結衣さん、結婚おめでとおおおおおお！！！！！')
