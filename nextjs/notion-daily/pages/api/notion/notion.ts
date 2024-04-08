import { Client } from "@notionhq/client";
import { NextApiRequest, NextApiResponse } from "next";

const notionSecret = process.env.NOTION_SECRET_KEY;
const notionDatabaseId = process.env.NOTION_DATABASE_ID_FINANCE_REPORT;

const notion = new Client({ auth: notionSecret });
export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (!notionSecret || !notionDatabaseId) {
    throw new Error("Missing notion secret or database ID");
  }

  const query = await notion.databases.query({
    database_id: notionDatabaseId,
  });
  console.log(query.results);
  res.status(200).json({query});
}
