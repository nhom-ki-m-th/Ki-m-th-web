# Test Cases - Chức năng Đăng nhập
## TC01 - Đăng nhập thành công
- **Các bước:**
  1. Mở trang /login
  2. Nhập username đúng
  3. Nhập password đúng
  4. Bấm nút Login
- **Dữ liệu nhập:**
  - Username: tomsmith
  - Password: SuperSecretPassword!
- **Kết quả mong đợi:**
  - Hiện thông báo: "You logged into a secure area!"

## TC02 - Sai mật khẩu
- **Các bước:**
  1. Mở trang /login
  2. Nhập username đúng
  3. Nhập password sai
  4. Bấm nút Login
- **Dữ liệu nhập:**
  - Username: tomsmith
  - Password: sai_mat_khau
- **Kết quả mong đợi:**
  - Hiện thông báo: "Your password is invalid!"

## TC03 - Sai tên đăng nhập
- **Các bước:**
  1. Mở trang /login
  2. Nhập username sai
  3. Nhập password đúng
  4. Bấm nút Login
- **Dữ liệu nhập:**
  - Username: sai_ten
  - Password: SuperSecretPassword!
- **Kết quả mong đợi:**
  - Hiện thông báo: "Your username is invalid!"