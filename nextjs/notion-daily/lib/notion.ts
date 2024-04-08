import { Client } from "@notionhq/client";
const apiKey = process.env.NOTION_SECRET_KEY;
const databaseId = process.env.NOTION_DATABASE_ID_FINANCE_REPORT;

const notion = new Client({
  auth: apiKey,
});

export const getDatabase = async () => {
  if (!databaseId) {
    throw new Error("No database ID provided");
  }
  const response = await notion.databases.query({
    database_id: databaseId,
  });
  console.log("response", response);
  return response.results;
};
