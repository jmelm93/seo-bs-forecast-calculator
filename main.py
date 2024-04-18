def seo_bs_forecast_calculator(current_traffic, max_traffic, change_type, impact_range, est_cvr, est_conv_value):
    """
    Calculate the forecasted revenue impact range of an SEO change.

    Args:
    - current_traffic (int): Current traffic per month.
    - max_traffic (int): Maximum potential traffic per month estimate.
    - change_type (str): Either "Positive" or "Negative".
    - impact_range (tuple): Tuple indicating the range of impact levels (e.g., (7, 10)).
    - est_cvr (float): Estimated conversion rate (as a percentage, e.g., 4.5 for 4.5%).
    - est_conv_value (float): Estimated conversion value (average revenue per conversion).

    Returns:
    - tuple: Estimated revenue impact range (min, max).
    """
    def calculate_revenue_impact(impact_level):
        # Calculate the maximum possible change in traffic
        if change_type.lower() == "positive":
            traffic_potential = max_traffic - current_traffic
            traffic_change = (traffic_potential * impact_level / 10)
        elif change_type.lower() == "negative":
            traffic_potential = current_traffic
            traffic_change = -(traffic_potential * impact_level / 10)
        else:
            raise ValueError("Change type must be either 'Positive' or 'Negative'.")

        # Calculate new traffic
        new_traffic = current_traffic + traffic_change

        # Calculate the conversion number and the revenue impact
        conversions = (new_traffic * est_cvr) / 100
        new_revenue = conversions * est_conv_value

        # Calculate the loss in revenue due to traffic loss
        current_conversions = (current_traffic * est_cvr) / 100
        current_revenue = current_conversions * est_conv_value

        return new_revenue - current_revenue

    # Calculate impacts at the lower and upper bounds of the impact range
    min_impact = calculate_revenue_impact(impact_range[0])
    max_impact = calculate_revenue_impact(impact_range[1])

    return (min_impact, max_impact)

if __name__ == "__main__":
    current_traffic = 50000  # Current traffic per month
    max_traffic = 120000     # Max potential traffic per month
    change_type = "Negative"  # Change type: "Positive" or "Negative"
    impact_range = (7, 10)    # Impact range from 1 to 10
    est_cvr = 2.0            # Estimated Conversion Rate (percentage)
    est_conv_value = 50      # Estimated Conversion Value ($)

    revenue_impact_range = seo_bs_forecast_calculator(current_traffic, max_traffic, change_type, impact_range, est_cvr, est_conv_value)
    print(f"\n Estimated Revenue Impact Range: ${revenue_impact_range[0]:,.2f} to ${revenue_impact_range[1]:,.2f} \n")
