import streamlit as st
st.image("Messenger_creation_31A83DBF-2988-4D1C-BCE6-BD631196D7FD.jpeg")
# ==============================
# CẤU HÌNH TRANG
# ==============================
st.set_page_config(
    page_title="Tính lãi tiết kiệm Nguyễn Ngọc Vân Anh",
    page_icon="💰",
    layout="centered"
)

# ==============================
# CSS GIAO DIỆN
# ==============================
st.markdown("""
<style>
    .main {
        background-color: #f7f9fc;
    }

    .title {
        text-align: center;
        color: #1f4e79;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 30px;
    }

    .result-box {
        background-color: #f0f7ff;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #1f77b4;
        margin-top: 15px;
    }

    .result-title {
        font-size: 18px;
        font-weight: bold;
        color: #1f4e79;
    }

    .result-value {
        font-size: 24px;
        font-weight: bold;
        color: #111;
    }
</style>
""", unsafe_allow_html=True)

# ==============================
# TIÊU ĐỀ
# ==============================
st.markdown(
    '<div class="title">💰 TÍNH LÃI GỬI TIẾT KIỆM NGUYỄN NGỌC VÂN ANH</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Công cụ tính nhanh tiền lãi và tổng số tiền nhận được</div>',
    unsafe_allow_html=True
)

# ==============================
# NHẬP DỮ LIỆU
# ==============================
st.header("📋 Thông tin khoản gửi")

col1, col2 = st.columns(2)

with col1:
    so_tien = st.number_input(
        "💵 Số tiền gửi (VNĐ)",
        min_value=0.0,
        value=100_000_000.0,
        step=1_000_000.0,
        format="%.0f"
    )

with col2:
    ky_han = st.number_input(
        "📅 Kỳ hạn (tháng)",
        min_value=1,
        max_value=120,
        value=12,
        step=1
    )

lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

# ==============================
# TÍNH TOÁN
# ==============================

if st.button("🧮 TÍNH LÃI", use_container_width=True):

    # Lãi suất dạng thập phân
    lai_suat_nam = lai_suat / 100

    # Thời gian gửi theo năm
    thoi_gian_nam = ky_han / 12

    # Tổng tiền lãi
    tong_tien_lai = so_tien * lai_suat_nam * thoi_gian_nam

    # Tiền lãi định kỳ
    if hinh_thuc == "Cuối kỳ":
        tien_lai_dinh_ky = tong_tien_lai
        so_ky = 1
        ten_ky = "cuối kỳ"

    elif hinh_thuc == "Hàng tháng":
        tien_lai_dinh_ky = so_tien * lai_suat_nam / 12
        so_ky = ky_han
        ten_ky = "tháng"

    else:  # Hàng quý
        tien_lai_dinh_ky = so_tien * lai_suat_nam / 4
        so_ky = ky_han / 3
        ten_ky = "quý"

    # Tổng tiền nhận được
    tong_goc_va_lai = so_tien + tong_tien_lai

    # ==============================
    # HIỂN THỊ KẾT QUẢ
    # ==============================
    st.success("✅ Đã tính toán thành công!")

    st.subheader("📊 Kết quả")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div class="result-box">
                <div class="result-title">💰 Tiền lãi định kỳ</div>
                <div class="result-value">
                    {tien_lai_dinh_ky:,.0f} VNĐ
                </div>
                <div>
                    Nhận vào mỗi {ten_ky}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="result-box">
                <div class="result-title">📈 Tổng tiền lãi</div>
                <div class="result-value">
                    {tong_tien_lai:,.0f} VNĐ
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    col3, col4 = st.columns(2)

    with col3:
        st.markdown(
            f"""
            <div class="result-box">
                <div class="result-title">🏦 Tiền gốc</div>
                <div class="result-value">
                    {so_tien:,.0f} VNĐ
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="result-box">
                <div class="result-title">💵 Tổng gốc + lãi</div>
                <div class="result-value">
                    {tong_goc_va_lai:,.0f} VNĐ
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ==============================
    # THÔNG TIN CHI TIẾT
    # ==============================
    st.divider()

    st.subheader("📝 Chi tiết khoản gửi")

    st.write(f"**Số tiền gửi:** {so_tien:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")

    if hinh_thuc == "Hàng tháng":
        st.info(
            f"Bạn nhận khoảng **{tien_lai_dinh_ky:,.0f} VNĐ/tháng** "
            f"trong {ky_han} tháng."
        )

    elif hinh_thuc == "Hàng quý":
        st.info(
            f"Bạn nhận khoảng **{tien_lai_dinh_ky:,.0f} VNĐ/quý** "
            f"trong {so_ky:.0f} quý."
        )

    else:
        st.info(
            f"Bạn nhận **{tong_tien_lai:,.0f} VNĐ tiền lãi** "
            f"vào cuối kỳ."
        )

# ==============================
# CÔNG THỨC
# ==============================
with st.expander("📚 Xem công thức tính"):

    st.markdown("""
    ### 1. Tổng tiền lãi

    **Tiền lãi = Tiền gốc × Lãi suất năm × Số tháng / 12**

    ### 2. Nhận lãi hàng tháng

    **Lãi tháng = Tiền gốc × Lãi suất năm / 12**

    ### 3. Nhận lãi hàng quý

    **Lãi quý = Tiền gốc × Lãi suất năm / 4**

    ### 4. Tổng tiền nhận được

    **Tổng tiền = Tiền gốc + Tổng tiền lãi**

    > Lưu ý: Đây là cách tính lãi đơn, phù hợp với trường hợp
    > tiền lãi được nhận định kỳ và không nhập vào tiền gốc.
    """)
