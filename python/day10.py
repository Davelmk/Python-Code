'''
图像化界面GUI
'''

import tkinter
import tkinter.messagebox


def main():
    flag = True
    # 修改标签文字

    def change_label_text():
        nonlocal flag
        flag = not flag
        if flag:
            color, msg = ('red', 'hello')
        else:
            color, msg = ('blue', 'goodbye')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('提示', '确认退出?'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    top.geometry()
    top.title('game')
    label = tkinter.Label(top, text='hello', font='Arial -32', fg='red')
    label.pack(expand=1)
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    tkinter.mainloop()


if __name__ == "__main__":
    main()
