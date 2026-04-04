class HUD:
    HUD_W = 54
    TOP = "╔" + "═" * HUD_W + "╗"
    SEP = "╠" + "═" * HUD_W + "╣"
    BOT = "╚" + "═" * HUD_W + "╝"

    def _row(self, text=""):
        return "║" + text.ljust(self.HUD_W) + "║"

    def _hp_bar(self, hp, max_hp, bar_len=10):
        filled = round(bar_len * hp / max_hp) if max_hp else 0
        return "[" + "█" * filled + "░" * (bar_len - filled) + "]"

    def render(self, player, enemies, max_enemies, combat_log):
        p = player

        print(self.TOP)

        bar = self._hp_bar(p.health_points, p.max_hp)
        print(self._row(f" {p.symbol}  Игрок"))
        print(
            self._row(
                f"    HP: {p.health_points}/{p.max_hp} {bar}"
                f"   ATK: {p.attack_damage//2} / {p.attack_damage} / {p.attack_damage*2}"
            )
        )

        print(self.SEP)

        for i in range(max_enemies):
            if i < len(enemies):
                e = enemies[i]
                bar = self._hp_bar(e.health_points, e.max_hp)
                print(
                    self._row(
                        f" {e.symbol}  {e.name:<10}"
                        f"  HP: {e.health_points}/{e.max_hp} {bar}"
                        f"  ATK: {e.attack_damage}"
                    )
                )
            else:
                print(self._row("    [повержен]"))

        print(self.SEP)

        log_lines = (combat_log + ["", ""])[:2]
        for line in log_lines:
            print(self._row(" " + line if line else ""))

        print(self.BOT)
        print("  [wasd / стрелки] движение   [q] выход")
