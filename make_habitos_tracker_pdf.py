from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth


OUT = "/Users/gyankashyap/Documents/Codex/2026-05-13/doctype-html-html-lang-en-head/HabitOS_Tracker_Explanation.pdf"
PAGE = (1280, 720)
W, H = PAGE

BG = colors.HexColor("#08070f")
PANEL = colors.HexColor("#171825")
TEXT = colors.HexColor("#fbfbff")
MUTED = colors.HexColor("#c8c6d8")
BLUE = colors.HexColor("#45caff")
PINK = colors.HexColor("#ff5faf")
GREEN = colors.HexColor("#32d583")
AMBER = colors.HexColor("#fdb022")
ORANGE = colors.HexColor("#ff8a3d")
RED = colors.HexColor("#ff5a7a")
LINE = colors.Color(1, 1, 1, alpha=0.14)


def draw_bg(c):
    c.setFillColor(BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(colors.Color(0.07, 0.08, 0.16, alpha=0.96))
    c.rect(0, H - 160, W, 160, fill=1, stroke=0)
    c.setFillColor(colors.Color(0.27, 0.79, 1.0, alpha=0.18))
    c.rect(0, H - 160, W * 0.42, 160, fill=1, stroke=0)
    c.setFillColor(colors.Color(1.0, 0.37, 0.69, alpha=0.13))
    c.rect(W * 0.42, H - 160, W * 0.30, 160, fill=1, stroke=0)
    c.setFillColor(colors.Color(0.20, 0.84, 0.51, alpha=0.14))
    c.rect(W * 0.72, H - 160, W * 0.28, 160, fill=1, stroke=0)


def title(c, kicker, heading, sub=None):
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(64, H - 66, kicker.upper())
    c.setFillColor(TEXT)
    c.setFont("Helvetica-Bold", 42)
    c.drawString(64, H - 116, heading)
    if sub:
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 18)
        c.drawString(64, H - 150, sub)


def footer(c, page):
    c.setFillColor(colors.Color(1, 1, 1, alpha=0.35))
    c.setFont("Helvetica", 11)
    c.drawRightString(W - 64, 38, f"HabitOS Tracker summary / {page}")


def panel(c, x, y, w, h, fill=PANEL, stroke=LINE):
    c.setFillColor(fill)
    c.roundRect(x, y, w, h, 10, fill=1, stroke=0)
    c.setStrokeColor(stroke)
    c.setLineWidth(1)
    c.roundRect(x, y, w, h, 10, fill=0, stroke=1)


def bullet_list(c, items, x, y, size=19, gap=34, color=TEXT):
    c.setFont("Helvetica", size)
    c.setFillColor(color)
    for item in items:
        c.setFillColor(GREEN)
        c.circle(x + 7, y + 7, 4, fill=1, stroke=0)
        c.setFillColor(color)
        c.drawString(x + 24, y, item)
        y -= gap


def wrapped(c, text, x, y, width, font="Helvetica", size=17, leading=24, color=TEXT):
    c.setFont(font, size)
    c.setFillColor(color)
    words = text.split()
    line = ""
    for word in words:
        test = word if not line else f"{line} {word}"
        if stringWidth(test, font, size) <= width:
            line = test
        else:
            c.drawString(x, y, line)
            y -= leading
            line = word
    if line:
        c.drawString(x, y, line)
        y -= leading
    return y


def metric_card(c, x, y, w, h, label, value, accent):
    panel(c, x, y, w, h, colors.Color(accent.red, accent.green, accent.blue, alpha=0.18))
    c.setFillColor(accent)
    c.rect(x, y, w, 6, fill=1, stroke=0)
    c.setFillColor(MUTED)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x + 22, y + h - 34, label)
    c.setFillColor(TEXT)
    c.setFont("Helvetica-Bold", 31)
    c.drawString(x + 22, y + 34, value)


def slide_1(c):
    draw_bg(c)
    title(c, "Overview", "HabitOS Tracker", "A simple daily habit dashboard built with one HTML file.")
    metric_card(c, 64, 410, 260, 120, "Purpose", "Track habits", BLUE)
    metric_card(c, 354, 410, 260, 120, "Data", "Real dates", GREEN)
    metric_card(c, 644, 410, 260, 120, "Storage", "Browser local", PINK)
    metric_card(c, 934, 410, 260, 120, "Setup", "No install", AMBER)
    panel(c, 64, 166, 1130, 180)
    wrapped(c, "The tracker helps you check off daily habits, earn XP, view today's progress, and see weekly or monthly consistency. It runs directly in the browser, so you can open index.html on your Mac without React, Node, or a backend server.", 94, 286, 1060, size=24, leading=34)
    footer(c, 1)


def slide_2(c):
    draw_bg(c)
    title(c, "User Flow", "How the tracker works", "The app turns small daily actions into progress, history, and streaks.")
    items = [
        ("Add or edit habits", "Name each habit and assign an XP value."),
        ("Check habits daily", "Each checked habit adds XP to today's progress."),
        ("Save by date", "The app stores today's completed habit IDs under today's date."),
        ("Render analytics", "Weekly and monthly sections read exact calendar dates."),
        ("Keep the streak", "A streak counts days with 70% or more progress.")
    ]
    y = 450
    for i, (head, body) in enumerate(items, 1):
        c.setFillColor([BLUE, GREEN, AMBER, PINK, ORANGE][i - 1])
        c.circle(92, y + 9, 17, fill=1, stroke=0)
        c.setFillColor(BG)
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(92, y + 3, str(i))
        c.setFillColor(TEXT)
        c.setFont("Helvetica-Bold", 24)
        c.drawString(130, y + 2, head)
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 18)
        c.drawString(130, y - 28, body)
        y -= 74
    footer(c, 2)


def slide_3(c):
    draw_bg(c)
    title(c, "Tech Stack", "What was used", "Everything is inside one portable front-end file.")
    panel(c, 64, 390, 350, 160)
    panel(c, 465, 390, 350, 160)
    panel(c, 866, 390, 328, 160)
    cards = [
        (94, 496, "HTML", "Builds the page structure: dashboard, form, habit list, stats, weekly and monthly views.", BLUE),
        (495, 496, "CSS", "Creates the colorful visual design, responsive layout, cards, progress bars, and mobile styling.", PINK),
        (896, 496, "JavaScript", "Handles adding, editing, deleting, checking habits, calculating XP, and saving history.", GREEN),
    ]
    for x, y, head, body, accent in cards:
        c.setFillColor(accent)
        c.setFont("Helvetica-Bold", 27)
        c.drawString(x, y, head)
        wrapped(c, body, x, y - 34, 270, size=16, leading=22, color=MUTED)
    panel(c, 64, 150, 1130, 170)
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 25)
    c.drawString(94, 265, "Storage model")
    wrapped(c, "The app uses localStorage with date keys like YYYY-MM-DD. Each day stores completed habit IDs and progress, so weekly and monthly data comes from real saved days instead of fake or random-looking rows.", 94, 226, 1050, size=19, leading=28, color=TEXT)
    footer(c, 3)


def slide_4(c):
    draw_bg(c)
    title(c, "Problem Areas", "Where things were breaking", "The first version worked visually, but the data model caused confusing behavior.")
    headers = ["Problem", "Why it happened", "Fix"]
    xs = [64, 395, 800]
    widths = [300, 370, 394]
    c.setFont("Helvetica-Bold", 17)
    for x, w, h in zip(xs, widths, headers):
        c.setFillColor(AMBER)
        c.drawString(x, 508, h)
        c.setStrokeColor(LINE)
        c.line(x, 492, x + w, 492)
    rows = [
        ("Add Habit did not work", "It used prompt popups, which can fail or feel hidden in embedded browsers.", "Replaced it with a real input form."),
        ("Weekly data looked random", "It used slice(-7) and then labeled records as Mon-Sun, even when dates did not match.", "Weekly view now uses actual current-week dates."),
        ("Monthly progress was wrong", "It reused weekly records instead of building a real month calendar.", "Monthly grid now reads real dates for the current month."),
        ("Habits stayed checked tomorrow", "Completion state lived on the habit itself, not inside a date entry.", "Completions now reset naturally by date."),
        ("Progress could become NaN", "Invalid or empty XP values were accepted.", "XP is validated from 1 to 999.")
    ]
    y = 455
    c.setFont("Helvetica", 15)
    for problem, why, fix in rows:
        panel(c, 52, y - 42, 1160, 54, colors.Color(1, 1, 1, alpha=0.035))
        wrapped(c, problem, 64, y, 300, size=15, leading=18)
        wrapped(c, why, 395, y, 370, size=15, leading=18, color=MUTED)
        wrapped(c, fix, 800, y, 370, size=15, leading=18, color=GREEN)
        y -= 66
    footer(c, 4)


def slide_5(c):
    draw_bg(c)
    title(c, "Final Logic", "How the fixed tracker calculates data", "The key improvement is simple: store progress by date.")
    panel(c, 64, 375, 520, 170)
    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(94, 495, "Daily calculation")
    bullet_list(c, [
        "Total XP = sum of all habit XP",
        "Earned XP = sum of checked habits",
        "Progress = earned XP / total XP",
        "Today saves completed habit IDs"
    ], 94, 455, size=17, gap=28)
    panel(c, 660, 375, 534, 170)
    c.setFillColor(PINK)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(690, 495, "History calculation")
    bullet_list(c, [
        "Week = Monday to Sunday dates",
        "Month = current month calendar",
        "Streak = days above 70%",
        "No saved date means no data"
    ], 690, 455, size=17, gap=28)
    panel(c, 64, 150, 1130, 145)
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(94, 248, "Main rule")
    wrapped(c, "The tracker never guesses old days. It only displays progress for dates that exist in saved history. That is why the weekly and monthly views are now reliable.", 94, 212, 1050, size=22, leading=32)
    footer(c, 5)


def slide_6(c):
    draw_bg(c)
    title(c, "Summary", "What you now have", "A clean, colorful habit tracker that runs directly on your Mac.")
    bullet_list(c, [
        "Single file app: paste the code into index.html and open it in a browser.",
        "Uses your original habits: sleep, deep study, exercise, homework, and guitar practice.",
        "Fully working actions: add, edit, delete, check habits, reset today.",
        "Real analytics: daily XP, progress, completed count, streak, week, month.",
        "Saved locally: data stays in the same browser and same file location."
    ], 90, 455, size=22, gap=44)
    panel(c, 64, 105, 1130, 105, colors.Color(0.20, 0.84, 0.51, alpha=0.13))
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 26)
    c.drawString(94, 162, "Best next improvement")
    c.setFillColor(TEXT)
    c.setFont("Helvetica", 20)
    c.drawString(94, 130, "Add backup/export so your localStorage data can be moved safely between browsers or folders.")
    footer(c, 6)


def main():
    c = canvas.Canvas(OUT, pagesize=landscape(PAGE))
    for slide in [slide_1, slide_2, slide_3, slide_4, slide_5, slide_6]:
        slide(c)
        c.showPage()
    c.save()
    print(OUT)


if __name__ == "__main__":
    main()
