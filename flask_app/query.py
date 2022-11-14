VALIDATE_CODES = \
    """ 
    SELECT code
    FROM   ports
    WHERE  ports.code = %s 
    """

GET_REGION_TREE_CODES = \
    """
    WITH recursive regions_tree
    AS (
        SELECT r.slug,
            r.parent_slug
        FROM regions r
        WHERE r.slug = %s
        
        UNION
        
        SELECT r.slug,
            r.parent_slug
        FROM regions_tree rt
        JOIN regions r ON rt.slug = r.parent_slug
        )
    SELECT p.code
    FROM ports p
    JOIN regions_tree r ON p.parent_slug IN (r.slug)
    """

GET_AVERAGE_PRICES = \
    """
    SELECT day,
        CASE 
            WHEN COUNT(price) >= 3
                THEN CAST(ROUND(AVG(price)) AS INT)
            ELSE 
                NULL
        END AS average_price
    FROM prices
    WHERE day BETWEEN %s AND %s
        AND orig_code IN %s
        AND dest_code IN %s
    GROUP BY day
    ORDER BY day
    """