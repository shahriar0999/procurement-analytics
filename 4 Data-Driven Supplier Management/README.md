# Real-World Make-vs-Buy Decision Cases.

## Understanding the Cost Equations First

### **Cost Structure Breakdown:**

**C_buy = c^buy_f + x · c^buy_v** (Equation 4.1)
- **c^buy_f**: One-time costs to set up buying (supplier search, contracts, quality audits)
- **c^buy_v**: Per-unit costs when buying (supplier price + transaction costs per unit)

**C_make = c^make_f + x · c^make_v** (Equation 4.2)  
- **c^make_f**: One-time costs to set up making (equipment, training, facility setup)
- **c^make_v**: Per-unit costs when making (materials + labor + overhead per unit)

---

Case 1: Always MAKE (Equation 4.3)
When: c^make_f ≤ c^buy_f AND c^make_v ≤ c^buy_v


### 🏢 **Real Example: Tesla's Battery Cell Production**

**Scenario:** Tesla decides whether to make battery cells in-house or buy from suppliers like Panasonic.

**Cost Analysis:**
- **Make Fixed Costs (c^make_f):** $2M (existing Gigafactory space, some equipment already available)
- **Make Variable Costs (c^make_v):** $80 per cell (raw materials, labor, utilities)
- **Buy Fixed Costs (c^buy_f):** $5M (supplier qualification, testing, supply chain setup)
- **Buy Variable Costs (c^buy_v):** $120 per cell (supplier price + logistics + quality control)

**Mathematical Check:**
- c^make_f ($2M) ≤ c^buy_f ($5M) ✓
- c^make_v ($80) ≤ c^buy_v ($120) ✓

**Result:** Tesla should ALWAYS MAKE regardless of volume because both setup costs and per-unit costs favor making.

**Business Logic:** Tesla has manufacturing expertise, economies of scale, and strategic control benefits.

---
