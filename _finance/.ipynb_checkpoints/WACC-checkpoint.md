---
layout: page
title: Weighted Average Cost of Capital (WACC)
---

<table>
<tr>
<th>Symbol</th>
<th>Definition</th>
</tr>
<tr>
<td>\(k_d\)</td>
<td>cost of debt capital</td>
</tr>
<tr>
<td>\(t_c\)</td>
<td>corporate tax rate</td>
</tr>
<tr>
<td>\(k_e\)</td>
<td>cost of equity capital</td>
</tr>
<tr>
<td>\(D\)</td>
<td>market value of debt</td>
</tr>
<tr>
<td>\(E\)</td>
<td>market value of equity</td>
</tr>
<tr>
<td>\(V=D+E\)</td>
<td>market value of assets</td>
</tr>
</table>

$$
\mathrm{WACC} = k_d(1-t_c) \cdot \dfrac{D}{V} + k_e \cdot \dfrac{E}{V}
$$

<iframe style="border: none" allow="fullscreen" src='https://graspablemath.com/canvas/embed.html?load=_39725d50befd67f5&options={"auto_resize_on_scroll": false, "use_toolbar": true, "undo_btn": true, "redo_btn": true, "new_sheet_btn": false, "font_size_btns": true, "formula_btn": false, "formula_panel": true, "help_btn": false, "help_logo_btn": true, "transform_btn": false, "keypad_btn": false, "scrub_btn": false, "draw_btn": false, "erase_btn": false, "arrange_btn": false, "reset_btn": true, "save_btn": false, "load_btn": false, "settings_btn": false, "share_btn": false, "insert_btn": false, "use_hold_menu": false, "display_labels": false, "btn_size": "xs", "ask_confirmation_on_closing": false, "vertical_scroll": true}' width="100%" height="500px"></iframe>

# WACC

> The cost of debt is 7% and the current outstanding debt is $1.4 million. The cost of equity is 14% and the D/E ratio is 1. The tax rate for businesses is 30%. What is the weighted average cost of capital?

$$
k_d = 0.07, t_c=0.3, D=1400000, k_e=0.14
$$

$$E=D$$ so $$\dfrac{D}{V}=\frac{1}{2}$$ and $$\dfrac{E}{V}=\dfrac{1}{2}$$.

$$
\mathrm{WACC} = (0.07)(1-0.3) \cdot \frac{1}{2} + (0.14) \cdot \frac{1}{2} = 0.0945
$$

# WACC

> A company has three bonds:
>
> 1.  Bond maturing in 2016, Market Value = 1.5 bn, Cost of debt = 2.45% 
>
> 2.  Bond maturing in 2019, Market Value = 2.1 bn, Cost of debt = 2.9%
>
> 3.  Bond maturing in 2025, Market Value = 1 bn, Cost of debt = 3.2% 
>
> If corporate tax rate is 0%, what is the WACC?

$$
V_1=1.5, V_2 = 2.1, V_3 = 1
$$

$$
V = V_1+V_2+V_3 = 4.6
$$

$$
w_1 = \dfrac{V_1}{V} = \frac{15}{46}, w_2 = \dfrac{V_2}{V} = \frac{21}{46}, w_3 = \dfrac{V_3}{V} = \frac{10}{46}.
$$

$$
c_1 = 0.0245, c_2 = 0.029, c_3 = 0.032
$$

$$
\mathrm{WACC} = w_1c_1 + w_2c_2 + w_3c_3 = 0.0282
$$


# Bond YTM

> YNB Ltd. acquired MOU Pty Ltd. 10 years ago. In order to fund this acquisition, YNB Ltd issued a bond. Currently it has an outstanding amount of $50,000,000 with maturity in 2 years. The bond has a coupon rate of 5% (payable annually). What is the current price of the bond given the YTM is 7%?

Annual coupon payment $$C=50000000\cdot0.05 = 2500000$$.

$$Y=0.07$$

$$\mathrm{PV} = \frac{C}{1+Y}+\frac{C}{\left(1+Y\right)^{2}}+\frac{50000000}{\left(1+Y\right)^{2}} = 48191981.83$$

