from typing import List
from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        i_name = [i for i in self.influencers if i.username == username]

        if influencer_type == 'PremiumInfluencer' or influencer_type == 'StandardInfluencer':
            if i_name:
                return f"{username} is already registered."
            if influencer_type == 'PremiumInfluencer':
                influencer = PremiumInfluencer(username, followers, engagement_rate)
            elif influencer_type == 'StandardInfluencer':
                influencer = StandardInfluencer(username, followers, engagement_rate)
            self.influencers.append(influencer)
            return f'{username} is successfully registered as a {influencer_type}.'
        else:
            return f"{influencer_type} is not an allowed influencer type."


    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        _id = [i for i in self.campaigns if i.campaign_id == campaign_id]

        if campaign_type == 'HighBudgetCampaign' or campaign_type == 'LowBudgetCampaign':
            if _id:
                return f'Campaign ID {campaign_id} has already been created.'
            if campaign_type == 'HighBudgetCampaign':
                campaign = HighBudgetCampaign(campaign_id, brand, required_engagement)
            elif campaign_type == 'LowBudgetCampaign':
                campaign = LowBudgetCampaign(campaign_id, brand, required_engagement)
            self.campaigns.append(campaign)
            return f'Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}.'
        else:
            return f"{campaign_type} is not a valid campaign type."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = [i for i in self.influencers if i.username == influencer_username]
        campaign = [c for  c in self.campaigns if c.campaign_id == campaign_id]
        if not influencer:
            return f"Influencer '{influencer_username}' not found."
        if not campaign:
            return f"Campaign with ID {campaign_id} not found."
        if not campaign[0].check_eligibility(influencer[0].engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        if influencer[0].calculate_payment(campaign[0]) > 0:
            campaign[0].budget -= influencer[0].calculate_payment(campaign[0])
            campaign[0].approved_influencers.append(influencer[0])
            influencer[0].campaigns_participated.append(campaign[0])
            return f"Influencer '{influencer_username}' has successfully participated " \
                   f"in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        total_reached_followers = {}

        for influencer in self.influencers:
            for campaign in influencer.campaigns_participated:
                reached_followers = influencer.reached_followers(type(campaign).__name__)
                total_reached_followers[campaign] = total_reached_followers.get(campaign, 0) + reached_followers

        return total_reached_followers

    def influencer_campaign_report(self, username: str):
        influencer = [i for i in self.influencers if i.username == username]
        if influencer:
            return influencer[0].display_campaigns_participated()

    def campaign_statistics(self):
        total_reached_followers = self.calculate_total_reached_followers()

        sorted_campaigns = sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget))

        campaign_stats = [
            f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, "
            f"Total budget: ${campaign.budget:.2f}, Total reached followers: {total_reached_followers.get(campaign, 0)}"
            for campaign in sorted_campaigns
        ]

        return f"$$ Campaign Statistics $$\n" + "\n".join(campaign_stats)


from project.influencer_manager_app import InfluencerManagerApp

manager = InfluencerManagerApp()

# Register influencers
print(manager.register_influencer("PremiumInfluencer", "JohnDoe", 50000, 4.2))
print(manager.register_influencer("StandardInfluencer", "JaneSmith", 10000, 3.5))
print(manager.register_influencer("PremiumInfluencer", "JohnDoe", 80000, 4.2))
print(manager.register_influencer("InvalidInfluencer", "JohnDoe", 50000, 4.2))
print(manager.register_influencer("StandardInfluencer", "AliceJohnson", 20000, 3.8))
print(manager.register_influencer("PremiumInfluencer", "OliviaBennett", 80000, 4.5))
print(manager.register_influencer("PremiumInfluencer", "DanielRodriguez", 90000, 4.8))
print(manager.register_influencer("PremiumInfluencer", "EmilyTurner", 1000000, 5.0))

# Create campaigns
print(manager.create_campaign("LowBudgetCampaign", 1, "TechGurus", 4.0))
print(manager.create_campaign("HighBudgetCampaign", 2, "FashionTrendz", 3.0))
print(manager.create_campaign("LowBudgetCampaign", 1, "FashionTrendz", 3.0))
print(manager.create_campaign("LowBudgetCampaign", 3, "QuantumFusion", 3.0))
print(manager.create_campaign("InvalidCampaign", 4, "FoodieDelights", 2.5))

# Participate in campaigns
print(manager.participate_in_campaign("JohnDoe", 1))
print(manager.participate_in_campaign("JaneSmith", 2))
print(manager.participate_in_campaign("AliceJohnson", 2))
print(manager.participate_in_campaign("AliceJohnson", 1))
print(manager.participate_in_campaign("NonExistentInfluencer", 1))
print(manager.participate_in_campaign("AliceJohnson", 3))
print(manager.participate_in_campaign("JohnDoe", 2))
print(manager.participate_in_campaign("JaneSmith", 4))
print(manager.participate_in_campaign("JaneSmith", 1))
print(manager.participate_in_campaign("OliviaBennett", 3))
print(manager.participate_in_campaign("DanielRodriguez", 3))
print(manager.participate_in_campaign("EmilyTurner", 3))

# Print influencer campaign reports and campaign statistics
print(manager.influencer_campaign_report("JohnDoe"))
print(manager.influencer_campaign_report("JaneSmith"))
print(manager.campaign_statistics())









