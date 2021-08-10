from app import db
from .models import Product

# This module is not run from within the application.  It is designed to import the products into an empty instance of the
# database via the flask shell on deployment after db initialization, migration, and upgrade via flask_migrate


def populate_products():
    name = "Breakfast Book"
    desc = "What's for breakfast?  You'll never know until you take a peak inside this dramatic adventure."
    price = 4.95
    sm_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091023/1-breakfast-2_litwuw.jpg"
    lg_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091023/1-breakfast-2_litwuw.jpg"
    product = Product(name, desc, price, sm_img, lg_img)
    db.session.add(product)
    db.session.commit()

    name = "Dowry Set"
    desc = "Have an eldest daughter you can't get off your hands?  Introduce her to the man of her dreams with our custom dowry set"
    price = 204.95
    sm_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091023/dowry-2_bhelon.jpg"
    lg_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091023/dowry-2_bhelon.jpg"
    product = Product(name, desc, price, sm_img, lg_img)
    db.session.add(product)
    db.session.commit()

    name = "Jazz Crabs"
    desc = "Love Crabs??? Love Jazz??? Have we got a deal for you.  Jazz crabs are perfect for any occassion!"
    price = 7.60
    sm_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091024/3-crabs-2_x6r8sh.jpg"
    lg_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091024/3-crabs-2_x6r8sh.jpg"
    product = Product(name, desc, price, sm_img, lg_img)
    db.session.add(product)
    db.session.commit()

    name = "Dead Animals"
    desc = "Love exterminating an entire species, but don't want to make Greta Thunberg angry? This is what you've been looking for!"
    price = 8.55
    sm_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091024/4-dead-2_pet36v.jpg"
    lg_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091024/4-dead-2_pet36v.jpg"
    product = Product(name, desc, price, sm_img, lg_img)
    db.session.add(product)
    db.session.commit()

    name = "Meat Thing"
    desc = "Ready for a burger themed McSnack?  Try our meat thing, you won't be disappointed!"
    price = 3.99
    sm_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091024/5-meat-2_g37omj.jpg"
    lg_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091024/5-meat-2_g37omj.jpg"
    product = Product(name, desc, price, sm_img, lg_img)
    db.session.add(product)
    db.session.commit()

    name = "Horse Juice"
    desc = "Need we say more?"
    price = 7.99
    sm_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091023/6-horse-2_e7oofz.jpg"
    lg_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091023/6-horse-2_e7oofz.jpg"
    product = Product(name, desc, price, sm_img, lg_img)
    db.session.add(product)
    db.session.commit()

    name = "Nyquill Jornan Rookie Card"
    desc = "This signed rookie card from the Chicago Balls will be the prized centerpeice of your collection!"
    price = 495.95
    sm_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091023/7-balls-2_bh4src.jpg"
    lg_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091023/7-balls-2_bh4src.jpg"
    product = Product(name, desc, price, sm_img, lg_img)
    db.session.add(product)
    db.session.commit()

    name = "Hairy Putter Costume"
    desc = "Just add magic and you will look like Hermany Granger.  One size fits owl."
    price = 5.55
    sm_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091023/8-Hermione-2_eros9l.jpg"
    lg_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091023/8-Hermione-2_eros9l.jpg"
    product = Product(name, desc, price, sm_img, lg_img)
    db.session.add(product)
    db.session.commit()

    name = "Cuss Pen"
    desc = "Get your f***ing cuss on! (Censored becuase I didn't want to open the pen and use it)"
    price = 6.66
    sm_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091024/9-cusspen-2_uejk1l.jpg"
    lg_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091024/9-cusspen-2_uejk1l.jpg"
    product = Product(name, desc, price, sm_img, lg_img)
    db.session.add(product)
    db.session.commit()

    name = "Print Ribs Only"
    desc = "If you've ever wanted to print the word ribs, now you can!"
    price = 22.22
    sm_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091024/10-printer-2_bejjd0.jpg"
    lg_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091024/10-printer-2_bejjd0.jpg"
    product = Product(name, desc, price, sm_img, lg_img)
    db.session.add(product)
    db.session.commit()

    name = "Floor Sandwhich"
    desc = "Get your grub on.  *grubs not necessarily included"
    price = 3.72
    sm_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091024/11-floor-2_ceh80u.jpg"
    lg_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091024/11-floor-2_ceh80u.jpg"
    product = Product(name, desc, price, sm_img, lg_img)
    db.session.add(product)
    db.session.commit()

    name = "Shaq Pregnancy Test"
    desc = "Been Shaqin up? This test will probably tell you if you are pregnant."
    price = 72.63
    sm_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091025/12-shaq-2_wlhnc5.jpg"
    lg_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091025/12-shaq-2_wlhnc5.jpg"
    product = Product(name, desc, price, sm_img, lg_img)
    db.session.add(product)
    db.session.commit()

    name = "Definitely Not Bugs"
    desc = "Definitely not a box of bugs - cures ennui"
    price = 8.39
    sm_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091025/13-capitalism-2_virnec.jpg"
    lg_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091025/13-capitalism-2_virnec.jpg"
    product = Product(name, desc, price, sm_img, lg_img)
    db.session.add(product)
    db.session.commit()

    name = "Frozen Celery"
    desc = "Cool off the heat of summer with this frozen treat kids will love!"
    price = 2.75
    sm_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091025/14-lickable-2_ivdorm.jpg"
    lg_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091025/14-lickable-2_ivdorm.jpg"
    product = Product(name, desc, price, sm_img, lg_img)
    db.session.add(product)
    db.session.commit()

    name = "Pickled Hair!"
    desc = "Just like mom used to make before she started drinking!"
    price = 0
    sm_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091023/15-hair-2_hinocq.jpg"
    lg_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091023/15-hair-2_hinocq.jpg"
    product = Product(name, desc, price, sm_img, lg_img)
    db.session.add(product)
    db.session.commit()

    name = "Shrek Sex Book"
    desc = "Wanna get your green freak on.  Cum to papa.  NSFW"
    price = 14.71
    sm_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091023/16-shrek-2_b9ruwy.jpg"
    lg_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091023/16-shrek-2_b9ruwy.jpg"
    product = Product(name, desc, price, sm_img, lg_img)
    db.session.add(product)
    db.session.commit()

    name = "Deoderant - Kevin"
    desc = "You'll probably smell like Kevin if you buy this item..."
    price = 13.24
    sm_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091023/17-kevin-2_vnr50x.jpg"
    lg_img = "https://res.cloudinary.com/coding-temple/image/upload/v1621091023/17-kevin-2_vnr50x.jpg"
    product = Product(name, desc, price, sm_img, lg_img)
    db.session.add(product)
    db.session.commit()
