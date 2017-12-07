# Django_Auth

#### 这是 Django 自带的授权 的一个简单的Demo


> 1. User 是可以扩展的 使用AUTH_USER_MODEL/AUTH_PROFILE_MODULE(这里不细讲)
> 2. User.objects.create_user(xxx) 创建用户
> 3. authenticate(req, username=username, password=password) 验证用户凭证
> 4. login(req, user) 登录
> 5. logout(req) 退出登录
> 6. @login_required 登录验证“过滤器”