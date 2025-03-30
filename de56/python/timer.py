import time #タイマー機能用
import tkinter as tk #ポップアップ表示用
from tkinter import messagebox #tkinterにはいくつか種類がありますが通常ポップアップはmessageboxを使用します

minutes=int(input("タイマーを設定する分数を入力してください："))
print(minutes,"分のタイマーを設定しました！")
timer=minutes*60 #入力された数値を秒から分に変換します

time.sleep(timer) #time.sleepで処理を一時停止します

#メインウィンドウを非表示にします
root = tk.Tk()
root.withdraw()

#ポップアップウィンドウの設定
root.attributes("-topmost", True)  #最前面に来るように固定します
messagebox.showinfo("タイマー", "入力した時間が経過しました。\n""いったん休憩しませんか？") #("ポップアップのタイトル", 表示メッセージ)

#プログラムを終了させます
root.destroy()