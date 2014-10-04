import random
from annoying.functions import get_object_or_None
from divided_kingdom.apps.game.models import Reward


def calculate_reward(player, event_action, success):

    reward = get_object_or_None(Reward, action=event_action, success=success)

    gold_reward_text = ""
    xp_reward_text = ""
    stamina_text = ""
    health_text = ""

    if reward:
        if reward.min_gold != 0:
            gold_amount = random.randint(reward.min_gold, reward.max_gold)

            if gold_amount > 0:
                gold_reward_text = "<BR>You gain <span class='gold'>{0} gold</span>.".format(gold_amount)
            else:
                gold_reward_text = "<BR>You lose <span class='gold'>{0} gold</span>.".format(gold_amount)

            player.gold += gold_amount

        if reward.XP > 0:
            player.xp += reward.XP
            xp_reward_text = "<BR>You gain <span class='xp'>{0} XP</span>.".format(reward.XP)

        if reward.health != 0:
            health_text = player.adjust_health(reward.health)

        if reward.stamina != 0:
            stamina_text = player.adjust_stamina(reward.stamina)

        player.save()

        return "{0}{1}<BR>{2}<BR>{3}".format(
            gold_reward_text, xp_reward_text, health_text, stamina_text)

    return ""