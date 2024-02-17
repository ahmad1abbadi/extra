import curses

def main(stdscr):
    # تعطيل عرض النص المدخل
    curses.curs_set(0)
    
    # تفعيل وضع النص المؤقت
    stdscr.timeout(100)
    
    # إعداد الشاشة
    stdscr.clear()
    stdscr.addstr(0, 0, "Press 'q' to quit")

    # إنشاء زر تفاعلي
    stdscr.addstr(2, 0, "Press me!", curses.A_REVERSE)
    stdscr.refresh()

    # انتظار الضغط على الزر
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == ord(' '):
            stdscr.addstr(3, 0, "Button pressed!")
            stdscr.refresh()

curses.wrapper(main)
##
