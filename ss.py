import curses

def main(stdscr):
    # تعطيل عرض النص المدخل
    curses.curs_set(0)

    # تفعيل وضع النص المؤقت
    stdscr.timeout(100)

    # إعداد الشاشة
    stdscr.clear()
    stdscr.addstr(0, 0, "Press 'q' to quit")

    # إنشاء قائمة من الأزرار
    buttons = ["Button 1", "Button 2", "Button 3"]
    selected_button = 0

    while True:
        # عرض الأزرار
        for i, button_label in enumerate(buttons):
            if i == selected_button:
                stdscr.addstr(2 + i, 0, f"> {button_label}", curses.A_REVERSE)
            else:
                stdscr.addstr(2 + i, 0, f"  {button_label}")

        stdscr.refresh()

        # انتظار الضغط على الأزرار أو استخدام الماوس
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key in [curses.KEY_UP, ord('k')]:
            selected_button = (selected_button - 1) % len(buttons)
        elif key in [curses.KEY_DOWN, ord('j')]:
            selected_button = (selected_button + 1) % len(buttons)
        elif key == ord('\n'):
            stdscr.addstr(5, 0, f"Button '{buttons[selected_button]}' pressed!")
            stdscr.refresh()
        
        # التحقق من استخدام الماوس
        _, mouse_x, mouse_y, _, _ = curses.getmouse()
        if 2 <= mouse_y < 2 + len(buttons):
            selected_button = mouse_y - 2

curses.wrapper(main)
###
