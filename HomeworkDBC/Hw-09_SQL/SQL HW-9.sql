-- HW 9
USE sakila;
-- 1a. Display the first and last names of all actors from the table actor.
SHOW FIELDS FROM actor;
SELECT first_name, last_name FROM actor;

-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name
SELECT concat(first_name, " ", last_name) as 'Actor Name'
FROM actor;
-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?
SELECT actor_id, first_name, last_name FROM actor WHERE first_name="Joe";

-- 2b. Find all actors whose last name contain the letters GEN:
SELECT actor_id, first_name, last_name FROM actor WHERE last_name like "%GEN%";

-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
SELECT last_name, first_name FROM actor WHERE last_name like "%LI%";

-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
SELECT country_id, country
from country
where country
in ('Afganistan', 'Bangladesh', 'China');

-- 3a. Keep a description of each actor: create a column in the table actor named <description> and use data type BLOB
ALTER TABLE actor
ADD Description BLOB;

-- 3b. Very quickly you realize that entering descriptions for each actor is too much effort. Delete the description column.
ALTER TABLE actor
DROP Description;

-- 4a. List the last names of actors, as well as how many actors have that last name.
select last_name, count(last_name) from actor
group by last_name

-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
select last_name, count(last_name) from actor
group by last_name
having count(last_name) >=2;

-- 4c. The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.
select first_name, last_name, actor_id
from actor
where last_name = "Williams";
update actor
set first_name="HARPO"
where actor_id=172; 

-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO.
update actor
set first_name="GROUCHO"
where actor_id=172; 

SELECT * FROM actor; 
-- ------------------------------

-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
create table address
	address id INT auto_increment NOT NULL,
    addresss VARCHAR(50) NOT NULL,
    addresss2 VARCHAR(50) NOT NULL,
    district VARCHAR(50) NOT NULL,
    city_id INT
    postal_code VARCHAR(10),
	phone VARCHAR(20) NOT NULL,
    location geometry
    last_update timestamp
    PRIMARY KEY(address_id) 
    );

-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
select s.first_name, s.last_name, a.address
from staff s
left join address a 
on (s.address_id = a.address_id);

-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
select s.staff_id, s.first_name, s.last_name
from staff s
join (select p.amount, p.payment_date sum(p.amount) 
	from payment p
    where date between '2005-08-01' and '2005-08-31')
on (p.staff_id = s.staff_id);

select  s.staff_id, s.first_name, s.last_name, p.amount, p.payment_date 
from staff s
right join (select s.staff_id, s.first_name, s.last_name, p.amount, p.payment_date 
	from payment p
	where date between '2005-08-01' and '2005-08-31')
on (p.staff_id = s.staff_id)
group by payment_date;

-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
select fa.film_id, fa.actor_id, f.title, count(fa.actor_id) as "Total Number of Actors in Film"
from film_actor fa
join film f
on (fa.film_id = f.film_id)
group by f.title;

-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
select count(film_id) as "Hunchback Impossible"
from inventory 
where film_id
in(select film_id
	from film 
	where title = "Hunchback Impossible");

-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
select c.first_name, c.last_name, c.customer_id, sum(amount) as "Total Customer Spend"
from customer c
join payment p
on (p.customer_id = c.customer_id)
group by customer_id
order by last_name ASC;

-- 7a The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q have also soared in popularity.  Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
select*from language;
select title
from film
where (language_id = 1)
AND (title like "Q%")
OR (title like "K%");

-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
select *
from actor a 
join film_actor fa
on(a.actor_id = fa.actor_id)
where film_id 
in (select film_id
	from film 
    where title = "Alone Trip");

-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.
-- couldn’t figure how to get all the Canadian locations; assuming it’s from the location field, but it’s a blob, don’t know how to extract data from that
select* from customer;
select* from address;

select *
	from customer c
	join address a
	on(c.address_id = a.address_id)
group by district; 

select district, address_id, city_id, count(district) from address
group by district
order by city_id;

-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as family films.
select rating, title 
from film
where (rating = "G")
OR (rating = "PG")
OR (rating = "PG-13");

-- 7e. Display the most frequently rented movies in descending order.
select * from rental;
SELECT count (r.inventory_id) AS "Number of Times Rented"
	FROM rental r
	JOIN film_text ft
	ON (ft.rental_id = r.rental_id)
	JOIN inventory i
	ON (i.inventory_id = r.inventory_id)
	JOIN film_text ft
	ON (s.store_id = i.store_id)
	group by r.inventory_id
	order by count(r.inventory_id) desc;
    
select rental_date, rental_date, inventory_id, count(inventory_id) as "Number of Times Rented"
from rental;
group by inventory_id;
join payment p
 on (p.rental_id = r.rental_id)
 
 -- 7f. Write a query to display how much business, in dollars, each store brought in.
create view total_sales as
SELECT s.store_id, SUM(amount) AS Gross
	FROM payment p
	JOIN rental r
	ON (p.rental_id = r.rental_id)
	JOIN inventory i
	ON (i.inventory_id = r.inventory_id)
	JOIN store s
	ON (s.store_id = i.store_id)
	GROUP BY s.store_id;

-- 7g. Write a query to display for each store its store ID, city, and country.
select s.store_id, c.city, co.country 
from city c
join address a
on c.city_id = a.city_id
join store s
on s.address_id = a.address_id
join country co
on co.country_id = c.country_id;

-- -------------------
-- 7h. List the top five genres in gross revenue in descending order. 
-- (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
select c.name, fc.film_id, fc.category_id, p.amount, i.inventory_id, sum(p.amount) as "Gross Revenue for Category"
from category c
join film_category fc
on fc.category_id = c.category_id
join inventory i
on i.film_id = fc.film_id
join rental r
on r. inventory_id = i.inventory_id
join payment p
on p.rental_id = r.rental_id
group by c.name
order by (p.amount) desc;

-- In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. 
-- Use the solution from the problem above to create a view. 
create view Top_Five_genre_by_gross_revenue as
select c.name, fc.film_id, fc.category_id, p.amount, i.inventory_id, sum(p.amount) as "Gross Revenue for Category"
from category c
join film_category fc
on fc.category_id = c.category_id
join inventory i
on i.film_id = fc.film_id
join rental r
on r. inventory_id = i.inventory_id
join payment p
on p.rental_id = r.rental_id
group by c.name
order by (p.amount) desc;

select * from Top_Five_genre_by_gross_revenue;
drop view Top_Five_genre_by_gross_revenue;

