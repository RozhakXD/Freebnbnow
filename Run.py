try:
    import requests, re, time, sys, os
    from rich import print as printf
    from rich.panel import Panel
    from rich.console import Console
except (ModuleNotFoundError) as e:
    __import__("sys").exit(f"[Error] {str(e).capitalize()}!")

COOKIES = {"SESSION": None}

class MAIN:
    def __init__(self) -> None:
        pass

    def COOKIES(self):
        global COOKIES
        try:
            os.system("cls" if os.name == "nt" else "clear")
            printf(
                Panel(
                    "\n[bold red]'||''''|                      '||              '||     \n ||  .                         ||               ||     \n ||''|   '||''| .|''|, .|''|,  ||''|, `||''|,   ||''|, \n ||       ||    ||..|| ||..||  ||  ||  ||  ||   ||  || \n[bold white].||.     .||.   `|...  `|...  .||..|' .||  ||. .||..|' \n           [underline green]Mining Speed ​​Claim - by Rozhak",
                    width=59,
                    style="bold bright_black",
                )
            )
            printf(
                Panel(
                    f"[bold white]Please fill in with `[bold green]freebnbnow[bold white]` account cookies, make sure you are logged in and the cookies\nare correct. You can use[bold red] Via Browser[bold white] to get Cookies!",
                    width=59,
                    style="bold bright_black",
                    title="> [Login Cookies] <",
                    subtitle="╭───────",
                    subtitle_align="left",
                )
            )
            self.YOUR_COOKIES = Console().input("[bold bright_black]   ╰─> ")
            if "freebnbnow_session" in self.YOUR_COOKIES:
                printf(
                    Panel(
                        f"[bold white]If you want to stop you can use[bold red] CTRL + Z[bold white] and if stuck use[bold green] CTRL + C[bold white]. However, if an\nerror occurs, your cookie may have expired!",
                        width=59,
                        style="bold bright_black",
                        title="> [Catatan] <",
                    )
                )
                while True:
                    try:
                        if COOKIES["SESSION"] != None:
                            self.DAPATKAN_MINING_SPEED()
                            continue
                        else:
                            COOKIES["SESSION"] = self.YOUR_COOKIES
                            continue
                    except (requests.exceptions.RequestException):
                        printf(
                            f"[bold bright_black]   ──>[bold green] YOUR CONNECTION IS HAVING A PROBLEM!          ",
                            end="\r",
                        )
                        time.sleep(10.0)
                        continue
                    except (KeyboardInterrupt):
                        printf(f"                                    ", end="\r")
                        time.sleep(2.5)
                        continue
            else:
                printf(
                    Panel(
                        f"[bold red]The cookie you entered is incorrect because it does not have `session=`, please try again!",
                        width=59,
                        style="bold bright_black",
                        title="> [Cookies Salah] <",
                    )
                )
                sys.exit()
        except (Exception) as e:
            printf(
                Panel(
                    f"[bold red]{str(e).capitalize()}!",
                    width=59,
                    style="bold bright_black",
                    title="> [Error] <",
                )
            )
            sys.exit()

    def DAPATKAN_MINING_SPEED(self):
        global COOKIES
        with requests.Session() as session:
            session.headers.update(
                {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Accept-Encoding": "gzip, deflate",
                    "Cache-Control": "max-age=0",
                    "Connection": "keep-alive",
                    "Cookie": "{}".format(COOKIES["SESSION"]),
                    "Host": "freebnbnow.com",
                    "Referer": "https://freebnbnow.com/dashboard",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Dest": "document",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-User": "?1",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                }
            )
            response = session.get("https://freebnbnow.com/dashboard")
            if "minutes from now" in str(response.text):
                try:
                    self.WALLET = re.search(
                        r"0x[a-fA-F0-9]{40}", str(response.text)
                    ).group(0)
                except (Exception):
                    self.WALLET = "null"
                printf(
                    Panel(
                        f"""[bold white]Status :[bold green] You get 25 TH/S!
[bold white]Link :[bold red] https://freebnbnow.com/rewards/6/click
[bold white]Miner Address :[bold blue] {self.WALLET}""",
                        width=59,
                        style="bold bright_black",
                        title="> [Sukses] <",
                    )
                )
                printf(
                    f"[bold bright_black]   ──>[bold yellow] PLEASE WAIT 60 MINUTES!                     ",
                    end="\r",
                )
                time.sleep(2.5)
                try:
                    self.MENIT = int(
                        re.search(
                            "Next: (\d+) minutes from now", str(response.text)
                        ).group(1)
                    )
                except (Exception):
                    self.MENIT = 60
                self.DETIK = self.MENIT * 60
                for SLEEP in range(self.DETIK, 0, -1):
                    time.sleep(1.0)
                    printf(
                        f"[bold bright_black]   ──>[bold white] WAIT[bold green] {SLEEP}[bold white] SECOND!                    ",
                        end="\r",
                    )
                return True
            elif 'href="https://freebnbnow.com/rewards/6/click"' in str(response.text):
                printf(
                    f"[bold bright_black]   ──>[bold green] CURRENTLY CLAIMING MINING SPEED!            ",
                    end="\r",
                )
                time.sleep(2.5)
                self.RESPONSE_COOKIES = "; ".join(
                    [
                        str(x) + "=" + str(y)
                        for x, y in session.cookies.get_dict().items()
                    ]
                )
                if "freebnbnow_session" in str(self.RESPONSE_COOKIES):
                    COOKIES["SESSION"] = f"{self.RESPONSE_COOKIES}"
                    session.headers.update({"Cookie": "{}".format(COOKIES["SESSION"])})
                    response2 = session.get("https://freebnbnow.com/rewards/6/click")
                    return True
                else:
                    printf(
                        f"[bold bright_black]   ──>[bold red] RESPONSE COOKIES NOT FOUND!                 ",
                        end="\r",
                    )
                    time.sleep(4.5)
                    COOKIES["SESSION"] = None
                    return False
            else:
                printf(
                    f"[bold bright_black]   ──>[bold red] FAILED WHEN CLAIMING MINING SPEED!          ",
                    end="\r",
                )
                time.sleep(5.5)
                COOKIES["SESSION"] = None
                return False

if __name__ == "__main__":
    try:
        os.system("git pull")
        MAIN().COOKIES()
    except (KeyboardInterrupt):
        sys.exit()