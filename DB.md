1、AutoField   ---自增列 = int(11)    如果没有的话，默认会生成一个名称为 id 的列，如果要显示的自定义一个自增列，必须将给列设置为主键 primary_key=True。
2、CharField   ---字符串字段  单行输入，用于较短的字符串，如要保存大量文本, 使用 TextField。必须 max_length 参数，django会根据这个参数在数据库层和校验层限制该字段所允许的最大字符数。
3、BooleanField   ---布尔类型=tinyint(1)   不能为空，Blank=True
4、ComaSeparatedIntegerField   ---用逗号分割的数字=varchar   继承CharField，所以必须 max_lenght 参数，
5、DateField   ---日期类型 date   对于参数，auto_now = True 则每次更新都会更新这个时间；auto_now_add 则只是第一次创建添加，之后的更新不再改变。
6、DateTimeField   ---日期类型 datetime   同DateField的参数
7、Decimal   ---十进制小数类型 = decimal   必须指定整数位max_digits和小数位decimal_places
8、EmailField   ---字符串类型（正则表达式邮箱） =varchar   对字符串进行正则表达式   一个带有检查 Email 合法性的 CharField，不接受 maxlength 参数。
9、FloatField   ---浮点类型 = double   浮点型字段。 必须提供两个 参数， 参数描述：
max_digits：总位数(不包括小数点和符号）
decimal_places：小数位数。如：要保存最大值为 999 (小数点后保存2位)，你要这样定义字段：FloatField(…，max_digits=5， decimal_places=2)，要保存最大值一百万(小数点后保存10位)的话，你要这样定义：FloatField(…，max_digits=19， decimal_places=10)
10、IntegerField   ---整形   用于保存一个整数
11、BigIntegerField   ---长整形

integer_field_ranges = {
    'SmallIntegerField': (-32768, 32767),
    'IntegerField': (-2147483648, 2147483647),
    'BigIntegerField': (-9223372036854775808, 9223372036854775807),
    'PositiveSmallIntegerField': (0, 32767),
    'PositiveIntegerField': (0, 2147483647),
}
12、IPAddressField   ---字符串类型（ip4正则表达式）   一个字符串形式的 IP 地址， (如 “202.1241.30″)。
13、GenericIPAddressField   ---字符串类型（ip4和ip6是可选的）   参数protocol可以是：both、ipv4、ipv6   验证时，会根据设置报错
14、NullBooleanField   ---允许为空的布尔类型   类似 BooleanField， 不过允许 NULL 作为其中一个选项。 推荐使用这个字段而不要用 BooleanField 加 null=True 选项。 admin 用一个选择框 　　　　<select> (三个可选择的值： “Unknown”， “Yes” 和 “No” ) 来表示这种字段数据。
15、PositiveIntegerField   ---正Integer   类似 IntegerField， 但取值范围为非负整数（这个字段应该是允许0值的…可以理解为无符号整数）
16、PositiveSmallIntegerField   ---正smallInteger  正小整型字段，类似 PositiveIntegerField， 取值范围较小(数据库相关)SlugField“Slug” 是一个报纸术语。 slug 是某个东西的小小标记(短签)， 只包　　含字母，数字，下划线和连字符。它们通常用于URLs。 若你使用 Django 开发版本，你可以指定 maxlength。 若 maxlength 未指定， Django 会使用默认长度： 50，它接受一个额外的参数：
prepopulate_from: 来源于slug的自动预置列表
17、SlugField   ---减号、下划线、字母、数字   它们通常用于URLs。
18、SmallIntegerField   ---数字   数据库中的字段有：tinyint、smallint、int、bigint.   类似 IntegerField， 不过只允许某个取值范围内的整数。(依赖数据库)
19、TextField   ---字符串=longtext ，一个容量很大的文本字段， admin 管理界面用 <textarea>多行编辑框表示该字段数据。
20、TimeField   ---时间 HH:MM[:ss[.uuuuuu]]   时间字段，类似于 DateField 和 DateTimeField。
21、URLField   ---字符串，地址正则表达式   用于保存URL。若 verify_exists 参数为 True (默认)， 给定的 URL 会预先检查是否存在(即URL是否被有效装入且没有返回404响应).
22、BinaryField   ---二进制
23、ImageField   ---图片   类似 FileField， 不过要校验上传对象是否是一个合法图片。用于保存图像文件的字段。其基本用法和特性与FileField一样，只不过多了两个属性height和width。默认情况下，该字段在HTML中表现为一个ClearableFileInput标签。在数据库内，我们实际保存的是一个字符串类型，默认最大长度100，可以通过max_length参数自定义。真实的图片是保存在服务器的文件系统内的。
height_field参数：保存有图片高度信息的模型字段名。width_field参数：保存有图片宽度信息的模型字段名。
使用Django的ImageField需要提前安装pillow模块，pip install pillow即可。
使用FileField或者ImageField字段的步骤：
在settings文件中，配置MEDIA_ROOT，作为你上传文件在服务器中的基本路径（为了性能考虑，这些文件不会被储存在数据库中）。再配置个MEDIA_URL，作为公用URL，指向上传文件的基本路径。请确保Web服务器的用户账号对该目录具有写的权限。
添加FileField或者ImageField字段到你的模型中，定义好upload_to参数，文件最终会放在MEDIA_ROOT目录的“upload_to”子目录中。
所有真正被保存在数据库中的，只是指向你上传文件路径的字符串而已。可以通过url属性，在Django的模板中方便的访问这些文件。例如，假设你有一个ImageField字段，名叫mug_shot，那么在Django模板的HTML文件中，可以使用{{object.mug_shot.url}}来获取该文件。其中的object用你具体的对象名称代替。
可以通过name和size属性，获取文件的名称和大小信息。

24、FilePathField   ---选择指定目录按限制规则选择文件，有三个参数可选， 其中”path”必需的，这三个参数可以同时使用， 参数描述：
path：必需参数，一个目录的绝对文件系统路径。 FilePathField 据此得到可选项目。 Example： “/home/images”；
match：可选参数， 一个正则表达式， 作为一个字符串， FilePathField 将使用它过滤文件名。 注意这个正则表达式只会应用到 base filename 而不是路径全名。 Example： “foo。*\。txt^”， 将匹配文件 foo23.txt 却不匹配 bar.txt 或 foo23.gif；
recursive：可选参数， 是否包括 path 下全部子目录，True 或 False，默认值为 False。
match 仅应用于 base filename， 而不是路径全名。 如：FilePathField(path=”/home/images”， match=”foo.*”， recursive=True)…会匹配 /home/images/foo.gif 而不匹配 /home/images/foo/bar.gif
25、FileField   ---文件上传字段。 要求一个必须有的参数： upload_to， 一个用于保存上载文件的本地文件系统路径。 这个路径必须包含 strftime formatting， 该格式将被上载文件的 date/time 替换(so that uploaded files don’t fill up the given directory)。在一个 model 中使用 FileField 或 ImageField 需要以下步骤：在你的 settings 文件中， 定义一个完整路径给 MEDIA_ROOT 以便让 Django在此处保存上传文件。 (出于性能考虑，这些文件并不保存到数据库。) 定义 MEDIA_URL 作为该目录的公共 URL。 要确保该目录对 WEB 服务器用户帐号是可写的。在你的 model 中添加 FileField 或 ImageField， 并确保定义了 upload_to 选项，以告诉 Django 使用 MEDIA_ROOT 的哪个子目录保存上传文件。你的数据库中要保存的只是文件的路径(相对于 MEDIA_ROOT)。 出于习惯你一定很想使用 Django 提供的 get_<fieldname>_url 函数。举例来说，如果你的 ImageField 叫作 mug_shot， 你就可以在模板中以 {{ object。get_mug_shot_url }} 这样的方式得到图像的绝对路径。
26、PhoneNumberField   ---一个带有合法美国风格电话号码校验的 CharField(格式：XXX-XXX-XXXX)
27、USStateField   ---美国州名缩写，由两个字母组成（天朝人民无视）。
28、XMLField   ---XML字符字段，校验值是否为合法XML的 TextField，必须提供参数：
schema_path：校验文本的 RelaxNG schema 的文件系统路径。


1、null   数据库中字段是否可以为空（null=True）
2、db_column  数据库中字段的列名(db_column="test")
3、db_tablespace
4、default  数据库中字段的默认值
5、primary_key  数据库中字段是否为主键(primary_key=True)
6、db_index  数据库中字段是否可以建立索引(db_index=True)
7、unique  数据库中字段是否可以建立唯一索引(unique=True)
8、unique_for_date  数据库中字段【日期】部分是否可以建立唯一索引
9、unique_for_month  数据库中字段【月】部分是否可以建立唯一索引
10、unique_for_year  数据库中字段【年】部分是否可以建立唯一索引
11、auto_now  更新时自动更新当前时间
12、auto_now_add  创建时自动更新当前时间
13、verbose_name  Admin中显示的字段名称
14、blankAdmin  中是否允许用户输入为空表单提交时可以为空
15、editableAdmin  中是否可以编辑
16、help_textAdmin  中该字段的提示信息
17choicesAdmin  中显示选择框的内容，用不变动的数据放在内存中从而避免跨表操作
18、validators 自定义错误验证（列表类型），从而定制想要的验证规则


<1>all():         查询所有结果
<2>filter(**kwargs)    它包含了与所给筛选条件相匹配的对象
<3>get(**kwargs):     返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。
<4>exclude(**kwargs)    它包含了与所给筛选条件不匹配的对象
<5>values(*field)     返回一个ValueQuerySet 一个特殊的QuerySet，运行后得到的并不是一系列model的实例化对象，而是一个可迭代的字典序列
<6>values_list(*field)   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
<7>order_by(*field)    对查询结果排序
<8>reverse()        对查询结果反向排序
<9>distinct()       从返回结果中剔除重复纪录
<10>count()        返回数据库中匹配查询(QuerySet)的对象数量。
<11>first()        返回第一条记录
<12>last()         返回最后一条记录
<13>exists()        如果QuerySet包含数据，就返回True，否则返回False
<14>annotate()       使用聚合函数
<15>dates()        根据日期获取查询集
<16>datetimes()      根据时间获取查询集
<17>none()         创建空的查询集
<18>union()        并集
<19>intersection()     交集
<21>difference()      差集
<22>select_related()    附带查询关联对象
<23>prefetch_related()   预先查询
<24>extra()        附加SQL查询
<25>defer()        不加载指定字段
<26>only()         只加载指定的字段
<27>using()        选择数据库
<28>select_for_update()  锁住选择的对象，直到事务结束。
<29>raw()         接收一个原始的SQL查询